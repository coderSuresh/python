student_heights= input("Enter the heights of students: ").split()
total_height =0
for height in student_heights:
    total_height+=int(height)
print(total_height)

numbercount = 0
for student in student_heights:
    numbercount+=1
print(numbercount)

average_height =round(total_height/numbercount)
print(average_height)