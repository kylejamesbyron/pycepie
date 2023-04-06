import sqlite3
connection = sqlite3.connect("recipes.db")
cursor = connection.cursor()

# To insert table
newTable = input("Recipe: ")

#input headers as list
cursor.execute("CREATE TABLE newTable (id INTEGER PRIMARY KEY AUTOINCREMENT, ingredient TEXT, amount INTEGER, genre TEXT, measure TEXT)") 
