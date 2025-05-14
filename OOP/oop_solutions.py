""" Create a Rectangle class with width and height attributes, and 
methods to calculate area and perimeter. """
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(5, 10)
print(rect.area())       # Output: 50
print(rect.perimeter())  # Output: 30





print("\n")
""" Create a Counter class that keeps track of a count value. Include 
methods to increment, decrement, and reset the counter. """
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def reset(self):
        self.value = 0

counter = Counter()
counter.increment()
counter.increment()
print(counter.value)  # Output: 2
counter.decrement()
print(counter.value)  # Output: 1
counter.reset()
print(counter.value)  # Output: 0





print("\n")
""" Create a Vehicle base class with attributes for make, model, and year. Then create a 
Car subclass that inherits from Vehicle and adds attributes for number of doors and fuel type."""
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, make, model, year, doors, fuel_type):
        super().__init__(make, model, year)
        self.doors = doors
        self.fuel_type = fuel_type

car = Car("Toyota", "Corolla", 2020, 4, "Gasoline")
print(car.make)   # Output: Toyota
print(car.doors)  # Output: 4





print("\n")
""" Create a BankAccount class with private attributes for balance and account number. Include 
methods for deposit, withdrawal, and checking balance. """
class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number  
        self.__balance = initial_balance        

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

account = BankAccount("123456", 1000)
print(account.get_balance())        # Output: 1000
account.deposit(500)
print(account.get_balance())        # Output: 1500
account.withdraw(200)
print(account.get_balance())        # Output: 1300
print(account.get_account_number()) # Output: 123456

try:
    account.__balance = 2000  
    print(account.__balance)  
except AttributeError:
    print("Cannot directly access private attribute")





print("\n")
""" 1. **Polymorphism and Abstract Classes**
    Create an abstract `Shape` class with an abstract method 
    for calculating area. Then implement concrete subclasses for 
    `Circle`, `Rectangle`, and `Triangle`."""
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4)
]

for shape in shapes:
    print(f"{type(shape).__name__} area: {shape.area():.2f}")





print("\n")
""" Design a simple library management system with classes for Book, Library, 
and Member. Books can be checked out by members, and the library keeps track of 
its inventory and checked-out books. """
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.books_issued = []

class Library:
    def __init__(self):
        self.available_books = []
        self.members = []
        self.issued_books = {}

    def add_book(self, book):
        self.available_books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def checkout(self, book, member):
        if book in self.available_books and book not in self.issued_books:
            self.issued_books[book] = member
            member.books_issued.append(book)

    def return_book(self, book, member):
        if self.issued_books.get(book) == member:
            del self.issued_books[book]
            member.books_issued.remove(book)

    def is_available(self, book):
        return book not in self.issued_books

library = Library()
book1 = Book("Python Basics", "John Smith")
book2 = Book("Algorithms", "Jane Doe")

library.add_book(book1)
library.add_book(book2)

m1 = Member("Alice", "M001")
library.register_member(m1)

library.checkout(book1, m1)
print(library.is_available(book1))  # Output: False
print(library.is_available(book2))  # Output: True

library.return_book(book1, m1)
print(library.is_available(book1))  # Output: True
