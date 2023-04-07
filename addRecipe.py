import sqlite3
connection = sqlite3.connect("recipes.db")
cursor = connection.cursor()

# To insert table
newTable = input("Recipe: ")

#input headers as list
cursor.execute("CREATE TABLE newTable (ingredient TEXT, amount INTEGER, measure TEXT)") 

cursor.execute("ALTER TABLE newTable RENAME TO ?") (newTable);

# try this Add [newTable] 
