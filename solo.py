# if  statement
import re
from itertools import product, permutations
from itertools import count
from itertools import chain, takewhile, accumulate
from ast import arg, pattern
import imp
import random
from tkinter.font import names
status = True
older = False
if (older and status):
    print("Hello World")
else:
    print("NOT ALLOWED")

if (not older):
    print("Hello World")

# while loop
i = 1
while i < 5:
    print(i)
    i += 1

# break statement
k = 1
while True:
    print(k)
    k += 1
    if k == 5:
        print("Breaking")
        break

# continue statement
i = 0
while i < 5:
    i += 1
    if i == 3:
        print("Skipping")
        continue
    print(i)


# calculate the total ticket price by skipping the ticket for under 3 age
total = 0
passengers = []
while True:
    age = int(input("Enter passenger's age \n"))
    passengers.append(age)
    size = len(passengers)
    if (size == 5):
        print(f"{size} passengers done")
        break

for age in passengers:
    if age > 3:
        total += 100

print(total)

# print numbers in range


def print_nums(x):
    for i in range(x):
        print(i)
        return


print_nums(10)

# search("Hello World", "hello")
text = input()
word = input()


def search(text, word):
    textList = text.lower().split(" ")
    wordLower = word.lower()
    if wordLower in textList:
        return "Word found"
    else:
        return "Word not found"


print(search(text, word))


def analyse(text):
    """Analyse the text and return the number of words and characters"""
    if text.isupper():
        return "ALL CAPS"


for i in range(5):
    value = random.randint(1, 6)
    print(value)


# exception handling
try:
    # this code will run if no exception is raised
    num = int(input("Enter a range number: "))
    divider = int(input("Enter a divider: "))
    for x in range(num):
        print(x/divider)
except ZeroDivisionError:
    # this code will run if a ZeroDivisionError exception is raised
    print("Division by zero is not allowed")
except ValueError:
    # this code will run if a ValueError exception is raised
    print("Invalid input")
finally:
    print("This will always run")

# Raising an exception


def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x/y


# assert statement
assert 1 == 1
assert (1 == 2), "1 is not equal to 2"

# working with files
with open("file.txt", "w") as f:
    f.write("Hello World")

# Book titles
file = open("/usercode/files/books.txt", "r")

# your code goes here
booksList = file.readlines()

for book in booksList:
    if book.endswith("\n"):
        book = book.strip("\n")
        print(f"{book[0]}{len(book)}")
    else:
        print(f"{book[0]}{len(book)}")


file.close()

# text analyzer


def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count


filename = input("Enter a filename: ")
with open(filename) as f:
    text = f.read()

for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * count_char(text, char) / len(text)
    print(f"{char}: {round(perc, 2)}%")

# longest word
txt = input()
# your code goes here
txtlist = txt.split(" ")
longest_word = ''
count = 0
for word in txtlist:
    if len(word) > count:
        count = len(word)
        longest_word = word

print(longest_word)

# High order function


def apply_twice(func, arg):
    return func(func(arg))


def add_five(x):
    return x + 5


print(apply_twice(add_five, 10))

# lambda function


def my_func(f, arg):
    return f(arg)


my_func(lambda x: x + 5, 10)

# lambda function of polynomial
print((lambda x: x**2 + 5*x + 4)(-6))

# map and filter
# map
nums = [11, 22, 33, 44, 55, 66, 77, 88, 99]


def add_five(x):
    return x + 5


newList = list(map(add_five, nums))
print(newList)

# filter
names = ["John", "Eric", "Jessica"]
res = list(filter(lambda str: str.endswith("n"), names))

# Generators


def countdown():
    i = 10
    while i > 0:
        yield i
        i -= 1


for i in countdown():
    print(i)

# decorators


def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap


@decor
def print_text():
    print("Hello World")


# itertools
# count

for i in count(3):
    print(i)
    if i > 20:
        break

newList = accumulate(range(8))
newList = list(newList)
newList
# output [0, 1, 3, 6, 10, 15, 21, 28]
lessThanSix = list(takewhile(lambda x: x <= 6, newList))
lessThanSix
# output [0, 1, 3, 6]
allTogether = list(chain(newList, lessThanSix))
allTogether
# output [0, 1, 3, 6, 10, 15, 21, 28, 0, 1, 3, 6]
test = list(accumulate([10, 20, 30, 40]))
test
# output [10, 30, 60, 100]
sum(test)
# output 200

letters = ("A", "B")
print(list(product(letters, range(2))))
# output [('A', 0), ('A', 1), ('B', 0), ('B', 1)]
print(list(permutations(letters)))
# output [('A', 'B'), ('B', 'A')]
a = {1, 2}
print(list(product(range(3), a)))
# output 6

# Fibonacci series
num = int(input())


def fibonacci(n):
    # complete the recursive function
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))


for i in range(num):
    print(fibonacci(i))

# OOP


class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        self.active = True
        self.online = False

    def info(self):
        msg = f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
        print(msg)

    def toggle_active(self):
        if(self.active):
            print("You are active :) do you want to be inactive? Enter Yes or No")
            state = input()
            if state == "Yes":
                self.active = False
                print("You are now inactive")
            elif state == "No":
                self.active = True
            else:
                print("Must be Yes or No")
        else:
            self.active = True
            print("You are now active")

    def toggle_online(self):
        if(self.online):
            self.online = False
            print("Offline")
        else:
            self.online = True
            print("Online")

    def status(self):
        stat = f"Active: {self.active} Online: {self.online}"
        print(stat)

# class and static methods

# classmethod


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)


square = Rectangle.new_square(5)
print(square.calculate_area())


# staticmethod
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples")
        else:
            return True


ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)
    print(pizza.toppings)


class Calculator:
    @staticmethod
    def add(x, y):
        return x + y


n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print(Calculator.add(n1, n2))

# property


class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @property
    def pineapple_allowed(self):
        return False  # read only property


# property with setter
class Number:
    def __init__(self, num):
        self.value = num
        self._available = False  # Weakly private attribute

    @property
    def isEven(self):
        if self.value % 2 == 0:
            return True
        else:
            return False

    @property
    def isAvailable(self):
        return self._available

    @isAvailable.setter
    def isAvailable(self, value):
        if value:
            password = input("Enter password: ")
            if password == "odalton!":
                self._available = value
            else:
                raise ValueError("Alert intruder")


x = Number(int(input()))
print(x.isEven)
print(x.isAvailable)
x.isAvailable = True
print(x.isAvailable)


# regular expression


pattern = r"spam"
text = "eggspamsausagespam"

if re.match(pattern, text):
    print("Match")
else:
    print("No match")

if re.search(pattern, text):
    print("Match")
else:
    print("No match")

newList = re.findall(pattern, text)
print(newList)

match = re.search(pattern, text)
print(match.group())
print(match.start())
print(match.end())
print(match.span())

str = "My name is Odalton"
pattern = r"Odalton"
newStr = re.sub(pattern, "Eric", str)
print(newStr)

# metacharacter . matches any character except newline
pattern = r"gr.y"
if re.match(pattern, "gray"):
    print("Match")
if re.match(pattern, "blue"):
    print("Match")
if re.match(pattern, "grey"):
    print("Match")

# metacharacters ^ and $ match the start and end of a string

pattern = r"^gr.y$"
if re.match(pattern, "gray"):
    print("Match")
if re.match(pattern, "stingray"):
    print("Match")

# character classes
pattern = r"[aeiou]"
if re.search(pattern, "grey"):
    print("Match")
if re.search(pattern, "qwertyuiop"):
    print("Match")


# regex for password
pattern = r"[a-zA-Z0-9]{8,}"
password = input("Enter password: ")

if re.match(pattern, password):
    print("Password created")
else:
    print("Wrong format")


# Write a program for your research that will take text as input and output all of
# the hashtags in it separately.
text = input()
# your code goes here
# use re.findall() with r"#\w+" as the regex
pattern = r"#\w+"
hashList = re.findall(pattern, text)
for i in hashList:
    print(i)

# Phone number validator starting with 1,8 or 9 and 8 digits long
pattern = r"^[189]\d{7}$"
phone = input("Enter phone number: ")
match = re.match(pattern, phone)
if match:
    print("Valid")
else:
    print("Invalid")
