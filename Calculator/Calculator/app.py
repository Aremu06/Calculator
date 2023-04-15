import requests as requests

import calculator
from calculator import add
import datetime
import os.path






numbers = [1, 2, 3, 4, 5,]
numbers.insert(6, 6)
print(len(numbers)) # length of array
for item in numbers:
    print(item)

# print in range

for numbers in range(5):
    print(numbers)


# print list by index

names = ["John", "Bob", "james", "sam", "kay"]
print(names[0:3])
print(names)

# while loop
i = 1
while i <= 5:
    print(i)
    i = i + 1


# variable
x = 3 < 2
print(x)



# if statement , we can have as manay as elif condition, else statement perform the last option

temperature = 25

if temperature > 30:
    print("its a hot day")
    print("Drink some water")
elif temperature > 20:
    print("its a nice day")
elif temperature > 10:
    print("its a cold day ")
else:
    print("its cold")
print("Done")



weight = int(input("weight: "))
unit = input("(K)g or (L)ls: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("weight in Lbs: " + converted)
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))


# Assignment operators with input
patient = 'John Smith'
age = 20
he_new_patient = True

print(patient, age, he_new_patient)


name = input("what is your name? ")
print("Hello " + name)



birth_year = input("What is your age? ")
age = 2023 - int(birth_year)
print(age)


first = int(input("first: "))
second = int(input("second: "))
sum = first + second
print(sum)


number = 10
message = "positive" if number > 0 else "0 or negative"
print(message)


#list
print(type([]))

numbers = [1, 2, 3, 4, -1, -20]
#numbers.sort()
#numbers.reverse()
#numbers.append(1000)
#print(len(numbers))
#numbers.clear()
#print(5 not in numbers)
numbers.remove(5)
numbers.pop() #pop remove the last elements from the list
del numbers [1] #another way of deleting element by index
del numbers [0:3] #another way of deleting element by range


#Set

numbersList = [1, 1] # duplicate is allowed
numbersSet = {1, 1} # in set duplicates are not allow
lettersSet = {"A", "A", "B", "C", "C"} # in set the order are not guarantee


#Set Union Intersection & Difference

lettersA = {"A", "B", "C", "D"}
lettersB = {"A", "E", "F"}

union = lettersA | lettersB
intersection = lettersA & lettersB
difference = lettersA - lettersB

print(f"Union = {union}") # union takes everything inside set and put them in another set
print(f"Intersection = {intersection}") # intersection is the common element btw lettersA & lettersB e.g A
print(f"Difference = {difference}") # everything in lettersA and not in lettersB e.g "B", "C",



#Dictionary allows us to store key value pairs and the key has to be unique

person = {
    "name": "james",
    "age": "20",
    "address": "UK"
}

print(person["name"])
print(person["age"])
print(person["address"])

print(person.keys())
print(person.values())
#person.clear()

print(person.get("age"))
person["age"] = 100 # this updade age value from 20 to 100

print(person)



# For loop help us to iterate through any data type or structure

names = ["Ahamed", "James",
         "Jay", "Marry"]

for name in names :
    print(name) # for loop in action



# loop through dictionary

person = {
    "name": "james",
    "age": "20",
    "address": "UK"
}

#for Key in person:
#    print(f"Key{Key} value:{person[Key]}")

for Key, value in person.items():
    print(f"Key{Key} value:{value}")

# exercise give the below list, loop and sum then print result

numbers = [1, 2, 3, 4, 5, 6, 7, 9]
result = 0

for number in numbers :
    result += number

print(f"Result = {result}")


# while loop is loop while a condition is true

number = 0

while number < 10:
    print(number)
    number += 1
else:
    print("while loop ended")



# Break & Continue

number = 0

# continue with for loop
for n in [1, 2, 3, 4, 5, 6, 7]:
    if n < 5:
        continue
    print(n)

# break
while number < 10:
    if number == 5:
        break
    number += 1
    print(number)

# continue
while number < 10:
    if number < 5:
        continue
    number += 1
    print(number)

# Function: function is a group of statement to perform a task and in side of the function we have a lot of logic

def greet():
    print("Hello how are you?")

greet()

# parameter and arguments : with function we can have argument

def greet(name, age): # name here is parameter
    print(f"Hello {name}how are you?")
    print(f"I know your age = {age}")

greet("James", age) # James here is an argument


# Return values from function

def is_adult(age):
    if age >= 16:
        return True
    else:
        return False

result = is_adult(10)
print(result)


def convertGender(gender="unknown"):
    if gender.upper() == "M":
        return "Male"
    elif gender.upper()== "F":
        return "Female"
    else: return f"Gender {gender} is unknow"

print(convertGender("F"))
print(convertGender("f"))
print(convertGender("M"))
print(convertGender("m"))


# Built-in function and import statement are build with the programming language to help in coding
# import allow us to import module within python e.g import math, you can import from modele instead of bringing the entire modeule e.g from math import isqrt

# Creating a modules- > create a calculator.py under the project root folder and define some function, then come back here and import calculator

print(calculator.divide(2, 2))
print(calculator.add(2, 2))
print(calculator.subtract(2, 2))
print(calculator.multiply(2, 2))

# Classes and Objects class is a blueprint that allow u to create object, from blueprint u can create many object. blueprint is specification of how things is been created
# with classes we specify the attributes, i.e module anything u want, behavior is what the object can do. the Object is the real things and how we create them is by using classes

class Phone:

    def __int__(self, brand, price):
        self.brand = brand
        self.price = price

    def call(self, phone_Number): # behavior of this phone
        print(f"{self.brand} is calling {phone_Number}")

iphone = Phone("Iphone 6s", 300)
samsung = Phone("samsung S20", 800)

print(iphone.brand) # properties
print(iphone.price) # properties
iphone.call("999") # behavior

print()

print(samsung.brand)
print(samsung.price)
samsung.call("99900009")

# working with dates

print(datetime.datetime.now())
print(datetime.date.today())
print(datetime.datetime.now().now())

# format date

now = datetime.datetime.now()
print(now)

print(now.strftime("%d %m %Y %H %M %S"))
print(now.strftime("%d/%m/%Y %H:%M:%S"))
print(now.strftime("%d-%m-%Y %H:%M:%S"))
print(now.strftime("%d-%B-%Y %H:%M:%S")) # this will format the date and get the exact full name of the month
print(now.strftime("%d-%b-%Y %H:%M:%S")) # this will format the date and get the abbreviation name of the month
print(datetime.date.today().strftime("%d-%m-Y"))


# creating file

# file = open("./data.csv", "W") # write only
# file = open("./data.csv", "a") # append the file
# file = open("./data.csv", "r") # reading
file = open("./data.csv", "r+") # read and write
file.write("id, name, email\n")
file.write("1, Jami, jamy@gmail.com\n")
# print(file.read()) #read the entire file
for line in file:
    print(line)

file.close()



# Better way to work with files

# with open("./data.csv", "r") as file:
#     print(file.read())

filename = "data.csv"

if os.path.isfile(filename):
    with open(filename, "r") as file:
        print(file.read())
else:
    print(f"file {filename} does not exit")


# fetching data from internet

from urllib import request
import json
r = request.urlopen("https://www.google.com")
print(r.getcode())
print(r.read())


# fetching joke from internet

url = "http;//official-joke-api.appspot.com/random_ten"

response = requests.get(url)
print(response.status_code)

jsonData =json.load(response.text)
print(jsonData)


class Joke:
    def __int__(self, setup, punchline):
        self.setup = setup
        self.punchline = punchline

    def __str__(self) -> str:
        return f"setup {self.setup} punchline {self.punchline}"

jokes = []

for j in jsonData:
    setup = j["setup"]
    punchline = j["punchline"]
    joke = Joke(setup, punchline)
    jokes.append(joke)

print(f"Got {len(jokes)} jokes")



# Pip and modules: pip is package manager for python

# Text to speech

import pyttsx3

for joke in jokes:
    print(joke)
    pyttsx3.speak("Setup")
    pyttsx3.speak(joke.setup)
    pyttsx3.speak("The Punchline")
    pyttsx3.speak(joke.punchline)
















