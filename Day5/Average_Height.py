# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
add_student_heights=0
for n in range(0,len(student_heights)):
  student_heights[n] = int(student_heights[n])
 # 🚨 Don't change the code above 👆
 #Write your code below this row 👇
  add_student_heights+=student_heights[n]
n=n+1
Total_average_student_height = round(add_student_heights/n)
print(Total_average_student_height)