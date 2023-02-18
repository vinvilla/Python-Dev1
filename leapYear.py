# Leap Year
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
Leap_flag = 0

if year % 4 == 0:
    Leap_flag = 1
    if year % 100 == 0:
        if year % 400 == 0:
            Leap_flag = 1
        else:
            Leap_flag = 0
    else:
        Leap_flag = 1
else:
    Leap_flag = 0

if (Leap_flag == 1):
    print ("Leap year.")
else:
    print ("Not leap year.")


# OR !!!
# if year % 4 == 0:
#     if year % 100 == 0:
#        if year % 400 == 0:
#           print ("Leap year.")
#        else:
#           print ("Not leap year.")
#     else:
#        print ("Leap year.")
#  else:
#    print ("Leap year.")
