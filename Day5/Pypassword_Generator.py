#Password Generator Project
import random
import string


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

print("Welcome to the PyPassword Generator!")
password_ask=int(input("How many letters would you like in your password?\n"))
symbols_ask = int(input("How many sumbol would you like?\n"))
number_ask = int(input("What many numbers would you like?\n"))
#Easy Level 
if(password_ask):
    password=""
    for passw in range(1,password_ask+1):  
      password+=random.choice(letters)
if(symbols_ask):
    symb=""
    for sym in range(1,symbols_ask+1):
        symb+=random.choice(symbols)
if(number_ask):
    num=""
    for number in range(1,number_ask+1):
        num+=random.choice(numbers)
print(num+symb+password)

#Hard Level 
# if(password_ask):
#     password_Lists=[]
#     password=""
#     for passw in range(1,password_ask+1):  
#       password_Lists.append(random.choice(letters))
# if(symbols_ask):
#     symb=""
#     for sym in range(1,symbols_ask+1):
#         symb+=random.choice(symbols)
# if(number_ask):
#     num=""
#     for number in range(1,number_ask+1):
# 
# num+=random.choice(numbers)
password=""
if(password_ask):
    password_Lists=[]

    for passw in range(1,password_ask+1):  
      password_Lists.append(random.choice(letters))

    for number in range(1,number_ask+1):
        password+=random.choice(numbers)
print(password_Lists)
random.shuffle(password_Lists)
print(password_Lists)

for pswd in password_Lists:
    password+=pswd    
print (password)