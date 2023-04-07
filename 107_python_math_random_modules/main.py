import math

#help(math)

value = 4.35
print(f" value : {value}")
print(f" math.floor(value) : {math.floor(value)}")  
print(f" math.ceil(value) : {math.ceil(value)}") 
print(f" round(value) : {round(value)}")    

#math pi ile from math import pi aynı şey
from math import pi

print(math.log(math.e))
print(math.log(100,10))
print(math.sin(10))
print(math.degrees(pi/2))
print(math.radians(180))

import random

print(random.randint(0,100))
random.seed(101)
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))



mylist = list(range(0,20))
print(mylist)

print(random.choice(mylist))

#Sample With Replacement
print(random.choices(population=mylist,k=10))


#Sample Without Replacement
print(random.sample(population=mylist,k=10))


mylist = ["apple", "banana", "cherry"]

print(random.choices(mylist, weights = [5, 2, 2], k = 14))


print(random.uniform(a=0,b=100))

print(random.gauss(mu=0,sigma=1))