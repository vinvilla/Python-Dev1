# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
j=int(0)

for i in range(0, n+1):
    j += student_heights[i]

print(int(round(j/(n+1),0)))
