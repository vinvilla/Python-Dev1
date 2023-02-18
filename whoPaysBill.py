#Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
random_integer = random.randint(1,len(names))
print(names[random_integer-1] + " is going to buy the meal today!")

person_who_will_pay = random.choices.(names)
