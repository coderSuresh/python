# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
small_pizza =15
medim_pizza =20
large_pizza =25
bill_with_cheese =0
bill_without_cheese=0
bill_with_pepperoni=0
bill_without_pepperoni=0
bill_with_extra_cheese=0
pepperoni_with_cheese=0
pepperoni_Wihout_cheese=0

if(size =="S"):
    bill=15
    if(add_pepperoni=="Y"):
        bill+=2
        bill_with_pepperoni=bill       
                    
        if(extra_cheese=="Y"):    
            pepperoni_with_cheese+=bill_with_pepperoni+1
            print(f"Your final bill is: ${pepperoni_with_cheese}.")
        else:                
            pepperoni_Wihout_cheese=bill_with_pepperoni
            print(f"Your final bill is: ${pepperoni_Wihout_cheese}.")
    else:           
        if(extra_cheese=="Y"):    
            bill+=1
            bill_with_cheese=bill     
            print(f"Your final bill is: ${bill_with_cheese}.")
        else:                
            bill_without_cheese=bill
            print(f"Your final bill is: ${bill_without_cheese}.")
if(size =="M"):
    bill=20
    if(add_pepperoni=="Y"):
        bill+=3
        bill_with_pepperoni=bill       
                    
        if(extra_cheese=="Y"):    
            pepperoni_with_cheese+=bill_with_pepperoni+1
            print(f"Your final bill is: ${pepperoni_with_cheese}.")
        else:                
            pepperoni_Wihout_cheese=bill_with_pepperoni
            print(f"Your final bill is: ${pepperoni_Wihout_cheese}.")
    else:           
        if(extra_cheese=="Y"):    
            bill+=1
            bill_with_cheese=bill     
            print(f"Your final bill is: ${bill_with_cheese}.")
        else:                
            bill_without_cheese=bill
            print(f"Your final bill is: ${bill_without_cheese}.")
elif(size =="L"):
    bill=25
    if(add_pepperoni=="Y"):
        bill+=3
        bill_with_pepperoni=bill       
                    
        if(extra_cheese=="Y"):    
            pepperoni_with_cheese+=bill_with_pepperoni+1
            print(f"Your final bill is: ${pepperoni_with_cheese}.")
        else:                
            pepperoni_Wihout_cheese=bill_with_pepperoni
            print(f"Your final bill is: ${pepperoni_Wihout_cheese}.")
    else:           
        if(extra_cheese=="Y"):    
            bill+=1
            bill_with_cheese=bill     
            print(f"Your final bill is: ${bill_with_cheese}.")
        else:                
            bill_without_cheese=bill
            print(f"Your final bill is: ${bill_without_cheese}.")
