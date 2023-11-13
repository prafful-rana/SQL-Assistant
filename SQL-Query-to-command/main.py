from langchain.llms import GooglePalm
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import SemanticSimilarityExampleSelector, FewShotPromptTemplate
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma 
from langchain.prompts.prompt import PromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt 
from dotenv import load_dotenv
import streamlit as st
import os
from fsl import fsl
load_dotenv()

def create_chain():
    llm = GooglePalm(google_api_key = os.getenv("GOOGLE_API_KEY"))

    db_user = 'root'
    db_password = 'root'
    db_host = 'localhost'
    db_name = 'atliq_tshirts'

    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}", sample_rows_in_table_info = 3)
    emb = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-miniLM-L6-v2')
    fsl_string = [ " ".join(i.values()) for i in fsl]
    vectorstore = Chroma.from_texts(fsl_string,embedding=emb, metadatas=fsl)
    example_selector = SemanticSimilarityExampleSelector(vectorstore = vectorstore, k=1)

    example_prompt = PromptTemplate(
    input_variables=["Question", "SQLQuery", "SQLResult","Answer",],
    template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
    )

    few_shot_prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix=_mysql_prompt,
    suffix=PROMPT_SUFFIX,
    input_variables=["input", "table_info", "top_k"], #These variables are used in the prefix and suffix
    )

    chain = SQLDatabaseChain.from_llm(llm,db,verbose = True, prompt = few_shot_prompt)
    return chain

if __name__ == "__main__":
    st.title("The T-Shirt Company : SQL Q&A")

    question = st.text_input("Enter your Question")
    if question:
        magic_box = create_chain()
        solution =  magic_box.run(question)
        st.header("Solution : ")
        st.write(solution)