from decimal import ROUND_HALF_DOWN
import random
import mymodule
random_integer=random.randint(1,100)
print(random_integer)
pi_value=mymodule.pi
print(pi_value)
random_float=round(random.uniform(1,5),2)
random_float=random.random()*5
print(random_float)
print(random.seed(10))