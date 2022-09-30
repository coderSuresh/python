import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
num_len=len(names)
choose_random_name =random.randint(0,num_len-1)
choosen_name=names[choose_random_name]
print(f"{choosen_name} is going to buy the meal today!")
#imprtant in list len() count after comma , such as alish, paras=> count 2

