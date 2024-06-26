#Basic structure 

#First we will make classes ! 

#1-library
#2-student


#Layers of abstraction 
#library 
#>> Available books
#>>Lend books
#>>Add books (Return or Back to the library )

#student 
#>>request books
#>>return books

import sys
class library:
    def __init__(self,listofbooks):
        self.availablebooks=listofbooks
    
    def displayavailablebooks(self):
        print("These books are available : ")
        for book in self.availablebooks:
            print(book)
    
    def lendbook(self,requestedbook):
        if requestedbook in self.availablebooks:
            print("You Borrowed this book ")
        else:
            print("Sorry this book is not available")
    def addbook(self, returnedbook):
        self.availablebooks.append(returnedbook)
        print("Thank you !")

class student :
    def requestbook(self):
        print ("Enter the name of the book which you want to request ")
        self.book=input()
        return self.book
    
    def returnbook(self):
        print("Enter the name of the book ,which you want to return : ")
        self.book=input()
        return self.book
    
def main():
    library = library(["Harry porter","Iron man","Freelancers in 2024"])
    student=student()
    done=False
    while done==False:
        print("""--Library Menu--
              1-Display all books
              2-Request book
              3-Return book
              4-Exit
              """)
        choice =int(input("Enter choice : "))
        if choice==1:
            library.displayavailablebooks()
        elif choice==2:
            library.lendbook(student.requestedbook())
        elif choice==3:
            library.addbook(student.returnbook())
        elif choice==4:
               sys.exit()

if __name__ == "__main__":
    main()