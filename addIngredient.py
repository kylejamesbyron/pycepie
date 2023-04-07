#add ingredient

# To add values
os.system('clear')
title = input("title: ")
author = input("author: ")
genre = input("genre: ")
description = input("description: ")
os.system('clear')
 print("RECORD TO REVIEW:")
 print('Title:')
  print(title)
        print('Author:')
        print(author)
        print('Genre:')
        print(genre)
        print('Description:')
        print(description)
        okay = input("Type OK to commit: ")
     #  To commit changes
        if okay == "OK":
    # To Insert Values
            cursor.execute("INSERT INTO media (title, author, genre, description) values (?, ?, ?, ?)", 
              (title, author, genre, description))
    #commit connection:
            connection.commit()