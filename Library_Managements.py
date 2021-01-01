class Library:
    def __init__(self,list,name):
        self.book_list = list
        self.name = name
        self.lendDict = {}

    def display_book(self):
        print(f"we have a following book in our library: {self.name}")
        for book in self.book_list:
            print(book)

    def lend_book(self,user,book):
        if book in self.book_list:
            if book not in self.lendDict.keys():
                self.lendDict.update({book:user})
                print("database has been updated. you can take the book now")
            else:
                print(f'the book "{book}" is being already used by {self.lendDict[book]}')
        else:
            print(f"{book} not found in our Database. Please enter valid book name.")
    def add_book(self,book):
        self.book_list.append(book)
        print("book has been added in the library")

    def return_book(self,book):
        if book in self.book_list:
            self.lendDict.pop(book)
        else:
            print("Enter the valid book name from the BookList")

if __name__ == '__main__':
    umang = Library(["Code Complete","The Pragmatic Programmer","Operating System","database manegement system"],"XYZW")

    while True:
        print("\n\n------------------*******------------------")
        print(f"welcome to {umang.name} library.\n\n")
        print("enter your choice to continue:")
        print("1. Display books")
        print("2. lend a book")
        print("3. add book")
        print("4. return book\n\n")

        user_choice = int(input("enter your choice:"))
        if user_choice not in [1,2,3,4]:
            print("enter the valid choice")
            continue
        elif user_choice == 1:
            umang.display_book()

        elif user_choice == 2:
            book = input("enter the name of the book you want to lend:")
            user = input("what's your good name?:")
            umang.lend_book(user,book)

        elif user_choice == 3:
            book = input("enter the name of the book you want to add:")
            umang.add_book(book)

        else:
            book = input("enter the name of the book you want to return:")
            umang.return_book(book)

        print("\npress 'q' for quit, and 'c' for continue:")

        user_choice2 = ''
        while user_choice2 != 'q' and user_choice2 != 'c':
            user_choice2 = input("your choice:")
            if user_choice2 == 'q':
                exit()

            elif user_choice2 == 'c':
                continue

            else:
                print("enter a valid input")
