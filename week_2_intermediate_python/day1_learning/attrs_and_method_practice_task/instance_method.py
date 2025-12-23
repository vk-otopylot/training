# Check Student Result Based on Marks

# class Student:
#     def __init__(self, name, mark):
#         self.name = name
#         self.mark = mark
#
#     def check_result(self):
#         if self.mark < 33:
#             print('Fail')
#         else:
#             print('Pass')
#
# s1 = Student('vivek', 56)
# s1.check_result()
# s2 = Student('shani', 32)
# s2.check_result()


# Deposit and Withdraw Money from a Bank Account

# class BankAccount:
#     balance = 1200
#     def deposit(self, amount):
#         self.balance = self.balance + amount
#         print(f'New Balance is {self.balance}')
#
#     def withdraw(self, amount):
#         self.balance = self.balance - amount
#         print(f'New Balance is {self.balance}')
#
# b1 = BankAccount()
# # b1.deposit(1000)
# b1.withdraw(1150)


# Library Book Information System :- Mixed all of Three topics

class LibraryBook:
    library_name = 'V.A.Kakadia Public Library'

    def __init__(self, book_title, author):
        self.book_title = book_title
        self.author = author

    def display_book_info(self):
        print("Library Name :", LibraryBook.library_name)
        print("Book Title   :", self.book_title)
        print("Author       :", self.author)

book1 = LibraryBook("Python Programming", "Guido van Rossum")
book2 = LibraryBook("Clean Code", "Robert C. Martin")
book1.display_book_info()
book2.display_book_info()