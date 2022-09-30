height=int(input("Enter your height: "))
age=int(input("Enter your age: "))
if height >= 120:
    bill=0
    print("Your are elligiable to ride rollercoster.")
    if age <12:
        bill=5
        print("Child tickets are : $5")
    elif age>=12 and age <= 18:
        bill=7
        print("Youth tickets are: $7")
    elif age>=45 and age <= 50:
        bill=0
        print(f"Total Bill Amount ${bill}")
    else:
        print("Adult tickets are: $12")
        bill=12        
    photo=input("Do you want to click Photos Y or N: ")
    if photo=="y":
        print("Add $3 To The Bill")
        bill+=3
        print("Total Bill Amount.",bill)
    elif photo=="n":
        #print("Total Bill Amount.$",bill)  
        print(f"Total Bill Amount ${bill}")      
else:
    print("Your are not elligiable to ride.")