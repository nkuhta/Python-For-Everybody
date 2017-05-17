##############################################################
####################    largest_so_far     ###################
##############################################################

#  Making Smart Loops
#  Trick = Thinking like a computer

#   1.  Set some variable
#   2.  Look for something or do something
#   3.  Look at the variables (payoff)

print("Before")
largest_so_far = -1

#  loop through an array
for thing in [9,41,12,3,74,15]:
    print(thing)
    if thing>largest_so_far:
        largest_so_far = thing
print("After")
print("largest_so_far = ",largest_so_far)

##############################################################
###############    Counting in a Loop     ####################
##############################################################
print("")
print("******************  Counting in a loop  ************")

#   zork is the Counting variable
zork=0
print("Before")

for thing in [9,41,12,3,74,15]:
    zork=zork+1
    print(zork, thing)
print('After')

##############################################################
################    Summing in a Loop     ####################
##############################################################
print("")
print("******************  Summing in a loop  ************")

#  running sum variable
zork = 0

print('before: ',zork)

for thing in [9,41,12,3,74,15]:
    #  adding each element = running total
    zork=zork+thing
    print("sum_so_far =",zork," array_val =",thing)
print('total sum =',zork)

##############################################################
################    Finding the Average     ##################
##############################################################
print("")
print("******************  Averaging in a loop  ************")

#  running sum and count variable
count = 0
summ=0

for thing in [9,41,12,3,74,15]:
    #  running total
    summ=summ+thing
    #  count iteration variable
    count=count+1

print('avergage =',summ/count)

##############################################################
################    Filtering in a Loop     ##################
##############################################################
print("")
print("******************  Filtering in a loop  ************")

print("before")

for value in [9,41,12,3,74,15]:
    if value>20:
        print('large number (>20): ',value)
print('after')

#  searching using Boolean

#  Change found if the search result finds the variable in question
found = False

print("")
print('before:',found)

for value in [9,41,12,3,74,15]:
    # change found to true if you find value==3
    if value==3:
        found=True
        #  make it smarter and faster with this break
        break
    print(found,value)

print('after:',found)
