# creating a generator that generates the squares of numbers up to some number N
def gensquare(N):
    for i in range(N):
        yield i*i

for square in gensquare(10):
    print(square)

print("-------")
# creating a generator that yields "n" random numbers between a low and high numbers.(that are inputs)
import random

def rand_num(n,low,high):
    for i in range(n):
        yield random.randint(low,high)

n = int(input("Enter the number of random numbers to generate: "))
low = int(input("Enter the lower bound of random numbers: "))
high = int(input("Enter the upper bound of random numbers: "))

generator = rand_num(n,low,high)

for number in generator:
    print(number)

print("--------")
# Using the iter() function to convert the string below into an iterator
s = 'hello'
s = iter(s)

print(next(s))
