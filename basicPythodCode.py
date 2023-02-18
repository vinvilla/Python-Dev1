print("Hello World")

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#1. Create a greeting for your program.
print("Welcome to Band Name Generator")
#2. Ask the user for the city that they grew up in.
city = input("Which city did you grow up in ? : \n")
#3. Ask the user for the name of a pet.
pet = input("Whats the name of your pet ? : \n") + "s"
#4. Combine the name of their city and pet and show them their band name.
print("The name of your band is : " + city + " " + pet)
#5. Make sure the input cursor shows on a new line:

Solution: https://replit.com/@appbrewery/band-name-generator-end


print("Welcome to the tip calculator.")
bill_amt = float(input("What was the total bill? $"))
num_guests = float(input("How many people to split the bill? "))
tip_pct = float(input("What percentage tip would you like to give? 10, 12, or15? "))
bill_amt = bill_amt * (1 + (tip_pct/100))
#ind_bill = round(bill_amt / num_guests,2)
ind_bill = ('%.2f'%(bill_amt / num_guests))
print("Each person should pay: $" + str(ind_bill))




# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
if len(two_digit_number) == 1:
    a = int(two_digit_number[0])
    b = 0
else:
    a = int(two_digit_number[0])
    b = int(two_digit_number[1])

c = a+b
print (str(a) + " + " + str(b) + " = " + str(c))
print (c)



# BMI
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = float(weight) / (float(height) ** 2)
print(int(bmi))



# AGE in weeks, months, days
# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_days = (90-int(age))*365
age_weeks = (90-int(age))*52
age_months = (90-int(age))*12
print(f"You have {age_days} days, {age_weeks} weeks, and {age_months} months left.")



#odd or even number
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if (int(number) % 2) == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

