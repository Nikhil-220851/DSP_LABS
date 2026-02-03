import math
import random
import re

class StudentData:
    def __init__(self, sid, name, marks):
        self.sid = sid
        self.name = name
        self.marks = marks
        self.percentage = 0
        self.grade = ""

    def calculate(self):
        self.percentage = sum(self.marks) / len(self.marks)
        if self.percentage >= 75:
            self.grade = "A"
        elif self.percentage >= 60:
            self.grade = "B"
        elif self.percentage >= 45:
            self.grade = "C"
        else:
            self.grade = "D"

    def display(self):
        print("ID:", self.sid)
        print("Name:", self.name)
        print("Percentage:", self.percentage)
        print("Grade:", self.grade)

sid = input("Enter Student ID: ")
name = input("Enter Student Name: ")
marks = list(map(int, input("Enter marks (space separated): ").split()))
s = StudentData(sid, name, marks)
s.calculate()
s.display()


class Employee:
    def __init__(self, eid, name, salary, doj):
        self.eid = eid
        self.name = name
        self.salary = salary
        self.doj = doj

    def display(self):
        print(self.eid, self.name, self.salary, self.doj)

e = Employee(46, "Nikhil", 50000, "21-02-2006")
e.display()


class ObjectCount:
    count = 0

    def __init__(self):
        ObjectCount.count += 1
        print("Total Objects:", ObjectCount.count)

o1 = ObjectCount()
o2 = ObjectCount()
o3 = ObjectCount()


class Sample:
    def __init__(self, a, b):
        self.a = a
        self.b = b

obj = Sample(10, 20)
print("Class Name:", obj.__class__.__name__)
print("Object ID:", id(obj))
print("Instance Variables:", obj.__dict__)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll):
        super().__init__(name, age)
        self.roll = roll

    def display(self):
        print(self.name, self.age, self.roll)

st = Student("Nikhil", 19, 46)
st.display()


class PersonMI:
    def person_details(self):
        print("Person details displayed")

class TeacherMI:
    def teacher_details(self):
        print("Teacher details displayed")

class Professor(PersonMI, TeacherMI):
    def display(self):
        self.person_details()
        self.teacher_details()

p = Professor()
p.display()


start = int(input("Enter start range: "))
end = int(input("Enter end range: "))
n = int(input("Enter how many numbers: "))
for i in range(n):
    print(random.randint(start, end))


r = float(input("Enter radius: "))
area = round(math.pi * r * r,2)
circumference = round(2 * math.pi * r,2)
print("Area:", area)
print("Circumference:", circumference)


phone = input("Enter phone number (XXX-XXX-XXXX): ")
pattern = re.compile(r"^\d{3}-\d{3}-\d{4}$")
if re.match(pattern, phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")


scores = list(map(int, input("Enter scores: ").split()))
scores.sort()
unique_scores = list(set(scores))
average = sum(scores) / len(scores)
print("Sorted Scores:", scores)
print("Without Duplicates:", unique_scores)
print("Average Score:", average)


class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print("Balance:", self.balance)

account =BankAccount("Nikhil")
n=1
print("Select the following operations to perform \n1)Withdrawl \n2)Deposit \n3)Check Balance \n4)Exit\n")
while(n == 1):
    m=int(input("Enter your option:"))
    if(m == 1):
        amount=int(input("Enter the amount to withdraw: "))
        account.withdraw(amount)
    elif(m==2):
        deposit=int(input("Enter the amount to deposit: "))
        account.deposit(deposit)
    elif(m == 3):
        account.check_balance()
    elif(m == 4):
        n=2
        print("Thank you for visiting!")
    else:
        print("Invalid option! try again")

class Book:
    def __init__(self, title):
        self.title = title
        self.available = True

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            self.borrowed_books.append(book.title)
            book.available = False
            print("Borrowed:", book.title)
        else:
            print("Book not available")

    def return_book(self, book):
        if book.title in self.borrowed_books:
            self.borrowed_books.remove(book.title)
            book.available = True
            print("Returned:", book.title)

b1 = Book("Data Science with Python")
b2 = Book("Computer organization and Architecture")
b3 = Book("Compile Design")
b4 = Book("Introduction to Operational Research")
m1 = Member("Nikhil")
m1.borrow_book(b1)
m1.borrow_book(b2)
m1.borrow_book(b4)
m1.borrow_book(b4)
m1.return_book(b1)
m1.return_book(b4)
