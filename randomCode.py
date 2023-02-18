# Generate Random Numbers
import random

random.seed(1)

# Get the state of the generator
state = random.getstate()

print('Generating a random sequence of 3 integers...')
for i in range(3):
    print(random.randint(1, 1000))

# Restore the state to a point before the sequence was generated
random.setstate(state)
print('Generating the same identical sequence of 3 integers...')
for i in range(3):
    print(random.randint(1, 1000))


#############################
#Generate Random Numbers
import random

i = 100
j = 20e7

# Generates a random number between i and j
a = random.randrange(i, j)
try:
    b = random.randrange(j, i)
except ValueError:
    print('ValueError on randrange() since start > stop')

c = random.randint(100, 200)
try:
    d = random.randint(200, 100)
except ValueError:
    print('ValueError on randint() since 200 > 100')

print('i =', i, ' and j =', j)
print('randrange() generated number:', a)
print('randint() generated number:', c)


#############################

import random

print('Random number from 0 to 1 :', random.random())
print('Uniform Distribution between [1,5] :', random.uniform(1, 5))
print('Gaussian Distribution with mean = 0 and standard deviation = 1 :', random.gauss(0, 1))
print('Exponential Distribution with lambda = 0.1 :', random.expovariate(0.1))
print('Normal Distribution with mean = 1 and standard deviation = 2:', random.normalvariate(1, 5))

#############################

import random

sequence = [random.randint(0, i) for i in range(10)]

print('Before shuffling', sequence)

random.shuffle(sequence)

print('After shuffling', sequence)


#############################
import random

a = ['one', 'eleven', 'twelve', 'five', 'six', 'ten']

print(a)

for i in range(5):
    print(random.choice(a))

#############################

import random

a = ['one', 'eleven', 'twelve', 'five', 'six', 'ten']

print(a)

for i in range(3):
    b = random.sample(a, 2)
    print('random sample:', b)


#############################

import random

random.seed(1)

print('Generating a random sequence of 4 numbers...')
print([random.randint(1, 100) for i in range(5)])

# Reset the seed to 1 again
random.seed(1)

# We now get the same sequence
print([random.randint(1, 100) for i in range(5)])



#############################

import random
random_integer = random.randint(1,10)
print('Generating a random number sequence ..')
print(random_integer)

#############################

import random
random_integer = random.randint(1,10)
print(random_integer)
random_float = random.random()
print(random_float)
random_float2 = random.randint(1,5)
print(random_float2)



#############################

# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
random_integer = random.randint(1,len(names))
print(names[random_integer-1] + " is going to buy the meal today!")

person_who_will_pay = random.choices.(names)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])

print(dirty_dozen)

print(dirty_dozen[0])
print(dirty_dozen[1])

print(dirty_dozen[1][2])
print(dirty_dozen[1][3])
