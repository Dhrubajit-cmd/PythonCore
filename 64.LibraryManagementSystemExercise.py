# Question :
'''
Write a library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and show how you can print
all books,add a book and get the number of books using different methods.Show that your program doesn't persist the books after the program is stopped.
'''

# Solution :

class Library :
   def __init__(self,books : list):
       self.books = books
   @property
   def Number_Of_Books(self):
       return len(self.books)

   def Print_Books(self):
       print(self.books)

   def Add_Book(self,new_book:str):
       added = self.books.append(new_book)
       print(self.books)

   def Remove_Book(self,remove_book:str):
       if remove_book in self.books :
        removed =  self.books.remove(remove_book)
        print(self.books)
       else :
           print(f"No Book named {remove_book} found in the library. \n")
book1 = Library(["Physics NCERT","Chemistry NCERT","Maths NCERT","SL ARORA"])

book1.Print_Books()
book1.Add_Book("SL ARORA Part:II ")
book1.Remove_Book("SL ARORA")
print(book1.Number_Of_Books)