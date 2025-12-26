import csv
from collections import defaultdict
from datetime import datetime

class BookNotAvailableError(Exception):
    pass

class MemberNotFoundError(Exception):
    pass

class Book:
    try:
        def __init__(self):
            self.books = []
            self.stock = defaultdict(int)
            self.load_books()

        def load_books(self):
            with open('books.csv', 'r') as file:
                csvreader = csv.DictReader(file)
                for data in csvreader:
                    self.books.append(data)
                    self.stock[data['book_id']] = data['available_copies']

        def save_books(self):
            fields = ['book_id', 'title', 'author', 'category', 'total_copies', 'available_copies']
            with open('books.csv', 'w', newline='') as file:
                csvwriter = csv.DictWriter(file, fieldnames=fields)
                csvwriter.writeheader()
                csvwriter.writerows(self.books)

        def add_book(self, book_id, title, author, category, total_copies, available_copies):
            data = {
                'book_id': book_id,
                'title': title,
                'author': author,
                'category': category,
                'total_copies': total_copies,
                'available_copies': available_copies
            }
            self.books.append(data)
            self.save_books()
            self.stock[book_id] = total_copies
            print('Book Added SuccessFully.!!!')

        def remove_book(self):
            book_id = input('Enter the book id you want to remove: ')
            for data in self.books:
                if not data['book_id'] == book_id:
                    raise BookNotAvailableError('The Book you entered is not available.')
                self.books.remove(data)
                self.stock.pop(book_id, None)
                self.save_books()
                print('Book Removed SuccessFully.')

        def search_book(self):
            title = input('Enter Title to Search: ').lower()
            for data in self.books:
                if not data['title'].lower() == title:
                    raise BookNotAvailableError('The Book you entered is not available.')
                print(data)

        def show_all_books(self):
            for data in self.books:
                print(data)

    except FileNotFoundError:
        print('Error: File does not exists.')
    except ValueError as v:
        print(v)
    except PermissionError:
        print('Error: You do not have permission to Read/Write to and from File.')
    except BookNotAvailableError as b:
        print(b)


class Member:
    try:
        def __init__(self):
            self.members = []
            self.load_member()

        def load_member(self):
            with open('members.csv', 'r') as file:
                csvreader = csv.DictReader(file)
                for data in csvreader:
                    self.members.append(data)

        def save_member(self):
            with open('members.csv', 'w', newline='') as file:
                fields = ['member_id', 'name', 'course', 'contact']
                csvwriter = csv.DictWriter(file, fieldnames=fields)
                csvwriter.writeheader()
                csvwriter.writerows(self.members)

        def register_member(self, member_id, name, course, contact):
            data = {
                'member_id': member_id,
                'name': name,
                'course': course,
                'contact': contact,
            }
            self.members.append(data)
            self.save_member()

        def view_member(self):
            m_name = input('Enter the member name: ').lower()
            for data in self.members:
                if not data['name'].lower() == m_name:
                    raise MemberNotFoundError('Error: Member not Found.')
                print(data)

        def list_all_members(self):
            for data in self.members:
                print(data)

    except FileNotFoundError:
        print('Error: File does not exists.')
    except ValueError as v:
        print(v)
    except PermissionError:
        print('Error: You do not have permission to Read/Write to and from File.')
    except MemberNotFoundError as m:
        print(m)


class LibrarySystem(Book,Member):
    try:
        def __init__(self):
            super().__init__()
            self.b_records = []
            self.load_records()

        def load_records(self):
            with open('borrow_records.csv', 'r') as file:
                csvreader = csv.DictReader(file)
                for data in csvreader:
                    self.b_records.append(data)

        def save_record(self):
            with open('borrow_records.csv', 'w', newline='') as file:
                fields = ['transaction_id', 'book_id', 'member_id', 'issue_date', 'return_date']
                csvwriter = csv.DictWriter(file, fieldnames=fields)
                csvwriter.writeheader()
                csvwriter.writerows(self.b_records)

        def issue_book(self, book_id, member_id, return_date=None):
            transaction_id = f"T{len(self.b_records) + 1}"
            issue_date = datetime.now().strftime("%Y-%m-%d")
            data = {
                'transaction_id': transaction_id,
                'book_id': book_id,
                'member_id': member_id,
                'issue_date': issue_date,
                'return_date': return_date,
            }
            self.stock['book_id'] -= 1
            self.b_records.append(data)
            self.save_record()

        def return_book(self, book_id, member_id):
            for data in self.b_records:
                if data['book_id'] == book_id and data['member_id'] == member_id and data['return_date'] == '':
                    data['return_date'] = datetime.now().strftime("%Y-%m-%d")
                    self.stock['book_id'] += 1
                    self.save_record()

        def add_book(self,book_id, title, author, category, total_copies, available_copies):
            super().add_book(book_id, title, author, category, total_copies, available_copies)

        def remove_book(self):
            super().remove_book()

        def show_books(self):
            super().show_all_books()

        def register_member(self,member_id, name, course, contact):
            super().register_member(member_id, name, course, contact)

        def show_members(self):
            super().list_all_members()


    except FileNotFoundError:
        print('Error: File does not exists.')
    except ValueError as v:
        print(v)
    except PermissionError:
        print('Error: You do not have permission to Read/Write to and from File.')




# b1 = Book()
# b1.add_book(101,'vivekbhai','vivekk','history',125,100)
# b1.add_book(102,'shanibhai','shanik','devayat khavad',225,100)
# b1.load_books()
# b1.remove_book()
# b1.search_book()
# b1.show_all_books()

# m1 = Member()
# m1.register_member(1001,'vivek','History',9484880483)
# m1.view_member()
# m1.list_all_members()

# ls1 = LibrarySystem()
# # ls1.issue_book(101,1001)
# ls1.return_book('101','1001')
# ls1.add_book(103,'hardeepbhai','hardeepd','self_discipline',225,180)

# print(type(ls1))