import sqlite3
connection = sqlite3.connect("recipes.db")
cursor = connection.cursor()

# To insert table
newTable = input("Recipe: ")

#input headers as list
cursor.execute("CREATE TABLE media (ingredient TEXT, amount INTEGER, measure TEXT)") 

# try this Add [newTable] 
