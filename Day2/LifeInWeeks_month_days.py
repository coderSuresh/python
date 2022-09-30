# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_as_int=int(age)
your_age_remaining= 90-age_as_int
days_remaining = your_age_remaining * 365
week_remaining = your_age_remaining *52
month_remaining =your_age_remaining * 12 
print(f"your have {days_remaining} days, and {week_remaining} weeks, and {month_remaining} month")