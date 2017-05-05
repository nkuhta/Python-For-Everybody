##############################################################
###############    Conditional Statements    #################
##############################################################

#  Execute code when certain specified conditions are true

#  Conditional Operators

#       <       Less Than
#       <=      Less Than or Equal
#       ==      Equal To?
#       >=      Greater Than or Equal
#       >       Greater Than
#       !=      Not Equal

#  Examples
x=5
if x==5:
    print('x=5')

if x > 4:
    print('Greater than 4')

if x >= 5:
    print('Greater than or Equal 5')

if x<6:print("Less than 6")

if x!=6:
    print("Not Equal 6")

##############################################################
###############    If Statement Structure    #################
##############################################################

#  if some_condition is true then do_something1,2,....
#  if some_condition is false skip doing something

#   if some_condition:
#       do_something1
#       do_something2
#        .
#        .
#        .

if x==5:
    print('Is 5')
    print('Is Still 5')
    print('Third 5')

print("check if x==6")
if x==6:
    print("x is 6")
    print("still 6")

print("after 6-check")

##############################################################
##############    for Statement Structure    #################
##############################################################


#  for some values of i do_something1,2,....

#   for i in range(#):
#       do_something1
#       do_something2
#        .
#        .
#        .

#  range(5) = [0 1 2 3 4]
#  range(1,5) = [1 2 3 4]
#  range(2,10,2) = [2,4,6,8]

for i in range(5):
    print("i = ",i)
    if i>2:
        print("Therefore: i > 2")
    print("Done with i = ",i)
