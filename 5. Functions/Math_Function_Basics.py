##############################################################
###################    Random Numbers    #####################
##############################################################

#  import the random number library
import random

#  print 10 random numbers between (0,1)
for i in range(10):
    #  define random number using random.random() call
    x=random.random()
    print(x)

#  Random integer between 5 and 10
r_int=random.randint(5,10)
print(r_int)

#  Random array value choice
t=[1.1,2.3,-3,44,56,6,7.1,89,.9,.10,311,.12]
print(t)
t_rand=random.choice(t)
print(t_rand)

##############################################################
###################     Math library     #####################
##############################################################
print("")
print("******************  math library  ************")

import math

#  print value of pi
print("pi = ",math.pi)
print("sin(pi) = ",math.sin(math.pi))
print("cos(pi) = ",math.cos(math.pi))
print("log10(100) =",math.log10(100))
print("log(100) =",math.log(100))
print("exp(4.60517) = ",math.exp(4.60517))
