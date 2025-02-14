i=30
type(i)

j='John'
type(j)

print("Hello World")



if(4>1):
  print("four is greater than 1")

#Variable declaration
#int
#comment
x=6
y="Hello World"
print(x)
print(y)

#changing value of variable
x=7
x="Malaika"
print(x)

a='Malaika'
b="Malaika"
c="""Malaika"""
d='''Malaika'''
#all are same

a=7
A="Malaika"
print (a)
print (A)
#A and a are two different variables(case-sensitive)

#Multiple variables
a,b,c = 1,2,3
print (a)
print (b)
print (c)

#assigning same value to variables
a=b=c=40
print (a)
print (b)
print (c)

#unpack a collection
subjects = ["AI", "MVC", "OS"]
x, y, z = subjects
print(x)
print(y)
print(z)

a="My"
b="name"
c="is"
d="Malaika"
print(a,b,c,d)

a=8
b=9
print(a+b)
#we cannot write var of diff datatypes like this



a=10
b="Hello World"
print(a,b)

#Global Variables
x="Aritifical Intelligence"

def test_function():
  print(x)

test_function()



x = "name"

def myfunc():
  x = "age"
  print("What is your " + x)

myfunc()

print("What is your " + x)

def myfunc():
  global a
  a = "fantastic"

myfunc()

print("Python is " + a)

y=int(2.8)
print(y)

#List allows duplication
subjectlist=["OS","MVC","AI","OS"]
print(subjectlist)
print(len(subjectlist))

#list with different datatypes
difflist=[1,2.6,"hello"]
print(difflist)
print(type(difflist))

#using list constructor to form a list
subjectlist=list(("OS","MVC","AI","OS"))
print(subjectlist)
print(subjectlist[1]) #accessing list elements



#Negative indexing
subjectlist=list(("OS","MVC","AI","OS"))
print(subjectlist[-2])

#range of index
print(subjectlist[1:3]) #index 3 won't be included

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

practupple=("hello",)
print(type(practupple))

newdict={'k':42, 'l':48, 'm':50}
print(newdict)

num = 25
if num%2 == 0:
    print("Even")
else:
  print("Odd")

i=3.8

int(i)
i

i=5
while i <=10:
  print(i)
  i= i+1

5>4



s='Hello'
type(s)

for i in "Hello":
  print (i)

class Stack:
    def __init__(self):
        self.stack = []

    # Push an element onto the stack
    def push(self, item):
        self.stack.append(item)

    # Pop an element from the stack
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    # Peek the top element of the stack
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Get the size of the stack
    def size(self):
        return len(self.stack)

# Example usage:
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Top element:", stack.peek())  # Output: 30
print("Popped element:", stack.pop())  # Output: 30
print("Stack size:", stack.size())  # Output: 2
print("Is stack empty?", stack.is_empty())  # Output: False



# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Accessing values using keys
print("Name:", my_dict["name"])  # Output: Alice
print("Age:", my_dict["age"])    # Output: 25

# Adding a new key-value pair
my_dict["profession"] = "Engineer"

# Updating an existing key-value pair
my_dict["age"] = 26

# Removing a key-value pair
del my_dict["city"]

# Checking if a key exists
if "name" in my_dict:
    print("Name is present in the dictionary")

# Iterating over dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Getting all keys and values
keys = my_dict.keys()
values = my_dict.values()

print("Keys:", keys)    # Output: dict_keys(['name', 'age', 'profession'])
print("Values:", values)  # Output: dict_values(['Alice', 26, 'Engineer'])

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements in a tuple (Indexing)
print("First element:", my_tuple[0])  # Output: 1
print("Last element:", my_tuple[-1])  # Output: 5

# Slicing a tuple
sub_tuple = my_tuple[1:4]
print("Sliced tuple:", sub_tuple)  # Output: (2, 3, 4)

# Tuples are immutable, so they cannot be modified directly.
# my_tuple[0] = 10  # This will raise an error: 'tuple' object does not support item assignment

# Length of a tuple
print("Length of the tuple:", len(my_tuple))  # Output: 5

# Concatenating tuples
new_tuple = my_tuple + (6, 7)
print("Concatenated tuple:", new_tuple)  # Output: (1, 2, 3, 4, 5, 6, 7)

# Iterating over a tuple
for item in my_tuple:
    print(item)
