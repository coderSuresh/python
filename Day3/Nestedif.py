height=int(input("Enter your height: "))
age=int(input("Enter your age: "))
if height >= 120:
    print("Your are elligiable to ride rollercoster.")
    if age <12:
        print("you have to pay: $5")
    elif age>=12 and age <= 18:
        print("you have to pay: $7")
    else:
        print("you have to pay: $12")
else:
    print("Your are not elligiable to ride.")