# Few Shot Learning

fsl = [{
    'Question' : 'How many Nike Shirts are Available?',
    'SQLQuery': "SELECT stock_quantity FROM t_shirts WHERE brand = 'Nike'",
    'SQLResult': "Result of the SQL Query",
    'Answer':'684'
    },
    {
    'Question':'How many Nike Shirts of size L are Available?',
    'SQLQuery':"SELECT SUM(stock_quantity) FROM t_shirts WHERE brand = 'Nike' and size = 'L'",
    'SQLResult':  "Result of the SQL Query",
    'Answer':'105'
    },
    {
    'Question' : 'What is the stock Quantity of NIKE size M?',
    'SQLQuery' : "SELECT SUM(stock_quantity) FROM t_shirts WHERE size = 'M' AND brand = 'Nike'",
    'SQLResult' : "Result of the SQL Query",
    'Answer' : '34'},
    {
    'Question' : 'What is the revenue generated after applying all the discounts?',
    'SQLQuery' : "select sum((price*(100-t)/100)*stock_quantity) from (select *,coalesce(lost_revenue.pct_discount,0) as t from (select price,stock_quantity,pct_discount from t_shirts left join discounts on t_shirts.t_shirt_id = discounts.t_shirt_id) as lost_revenue) as t ;",
    'SQLResult' : "Result of the SQL Query",
    'Answer' : '81861.3'
    },
    {
    'Question' : 'I Have an order for 3 M sized Nike and 12 XS sizes Van Heusen Tshirts, Can I fulfil the order?',
    'SQLQuery' : "SELECT stock_quantity FROM t_shirts WHERE size = 'M' AND brand = 'Nike' AND stock_quantity >= 3 UNION ALL SELECT stock_quantity FROM t_shirts WHERE size = 'XS' AND brand = 'Van Huesen' AND stock_quantity >= 12",
    'SQLResult' : "Result of the SQL Query",
    'Answer' : 'Yes'
    },
    {
    'Question' : 'How much money is lost due to discounts?',
    'SQLQuery' : "select sum((price*(t)/100)*stock_quantity) from (select *,coalesce(lost_revenue.pct_discount,0) as t from (select price,stock_quantity,pct_discount from t_shirts left join discounts on t_shirts.t_shirt_id = discounts.t_shirt_id) as lost_revenue) as t ",
    'SQLResult' : "Result of the SQL Query",
    'Answer' : '3115.7'
    },
    {
        "Question": "'How much revenue is generated from Nike t_shirts after applying discount?'",
        "SQLQuery" : "select sum((price*(100-pct_discount)/100)*stock_quantity) from (select price,stock_quantity,pct_discount from t_shirts left join discounts on t_shirts.t_shirt_id = discounts.t_shirt_id where brand = 'Nike') as t; ",
        'SQLResult' : "Result of the SQL Query",
        'Answer' : '2431.4'
    }
]