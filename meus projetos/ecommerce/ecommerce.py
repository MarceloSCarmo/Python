import mysql.connector

# importando base de dados do mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mar.123sud",
  database="bike"
)
# executando a query
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM product")

# lendo a lista de produtos
numLinha = 1;
while numLinha <= 10:
   product_Lista = mycursor.fetchone()
   print(product_Lista)
   
   numLinha += 1