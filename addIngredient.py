#add ingredient

# To add values

ingredient = input("ingredient: ")
amount = input("amount: ")
measure = input("measure: ")

print("RECORD TO REVIEW:")
print('ingredient:')
print(ingredient)
print('amount:')
print(amount)
print('measure:')
print(measure)
okay = input("Type OK to commit: ")
 #  To commit changes
if okay == "OK":
# To Insert Values
	cursor.execute("INSERT INTO media (ingredient, amount, measure) values (?, ?, ?)", 
              (ingredient, amount, measure))
    #commit connection:
	connection.commit()
else:
	print("Cancelled")

