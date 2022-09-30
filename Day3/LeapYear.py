# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#  divided by 100 means a century year
# year divided by 400 is a leap year
if(year%400==0 and year%100==0):#for century year 
    print("Leap year.")
# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif(year%4==0 and year%100!=0):
    print("Leap year.")   
# not divide by 400 and 40 means not a leap year
else:
    print("Not leap year.")