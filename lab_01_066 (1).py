# -*- coding: utf-8 -*-
"""Lab 01-066.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GlktR_UQBe48XOon3E8EYKKO7OG9kNX8
"""



"""#Activity 01"""

n = int(input ("Enter a number: "))
if n % 2 == 0:
    print("The given number is even")
else:
    print("The given number is odd")

"""#Activity 02"""

summ=0
s=int(input("Enter an integer value: "))


while s!=0:
  summ=summ+s
  s=int(input("Enter an integer value: "))

print(summ)

"""#Activity 3"""

from re import I
primeno=True
i=2
n=int(input("Enter a number: "))

while i<n:
  remainder=n%i
  if remainder==0:
    primeno=False
    break

  else:
    i=i+1

if primeno:
  print("Number is prime")

else:
  print("Number is not prime")

"""#Activity 4"""

i=0
summ=0
while i<5:
  n=int(input("Enter 5 numbers: "))
  summ=summ+n
  i=i+1

print("sum is : ",summ)

"""#Activity 5"""

summation=0
i=1
while i<=10:
  summation=summation+i
  i=i+1

print ("sum is ",summation)

"""#Activity 5(other option)"""

n=int(input("Enter a number: "))
print("sum {}".format(n*(n+1)/2))

"""#Activity 7"""

import random

# Awroken

MINIMUM = 1
MAXIMUM = 9
NUMBER = random.randint(MINIMUM, MAXIMUM)
GUESS = None
TRY = 0
RUNNING = True

print("Alright...")

while RUNNING:
    GUESS = input("What is your lucky number? ")  # Changed raw_input to input for Python 3

    if GUESS.lower() == "exit":  # Moved exit check before int conversion
        print("Better luck next time.")
        break

    if not GUESS.isdigit():  # Ensure input is a valid number
        print("Please enter a valid number.")
        continue

    GUESS = int(GUESS)

    if GUESS < NUMBER:
        print("Wrong, too low.")
    elif GUESS > NUMBER:
        print("Wrong, too high.")
    elif GUESS == NUMBER:
        print("Yes, that's the one, %s." % str(NUMBER))
        if TRY < 2:
            print("Impressive, only %s tries." % str(TRY))
        elif 2 <= TRY < 10:
            print("Pretty good, %s tries." % str(TRY))
        else:
            print("Bad, %s tries." % str(TRY))
        RUNNING = False  # Stop the loop
    TRY += 1

"""#Lab Task 1"""

num = int(input("Enter an integer: "))
reverse= 0

while num != 0:
    digit = num % 10
    reverse = reverse* 10 + digit
    num //= 10

print("Reversed number:", reverse)

"""#Lab Task 2"""

numbers=[1,2,3,4,5,6]
even=0
odd=0
for num in numbers:
  if num%2==0:
    even=even+num

  else:
    odd=odd+num
print("Sum of even numbers is ",even)
print("Sum of odd numbers is ",odd)

"""#Lab Task 3 (Iterative)

"""

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

num_terms = int(input("Enter the number of terms: "))
print("Fibonacci series is:")
fibonacci(num_terms)

"""#Lab Task 3 (Recursive)"""

def fibonacci(n, a=0, b=1):
    if n > 0:
        print(a, end=" ")
        fibonacci(n - 1, b, a + b)

print("\nFibonacci series is: ")
fibonacci(num_terms)

"""#Lab Task 4

"""

marks = int(input("Enter marks (1-100): "))

if marks < 50:
    print("F")
elif 50 <= marks <= 60:
    print("E")
elif 61 <= marks <= 70:
    print("D")
elif 71 <= marks <= 80:
    print("C")
elif 81 <= marks <= 90:
    print("B")
elif 91 <= marks <= 100:
    print("A")
else:
    print("Invalid marks")

"""#Lab Task 5"""

num = int(input("Enter a number: "))

factorial = 1
for i in range(1, num + 1):
    factorial *= i

print("Factorial of", num, "is", factorial)