##############################################################
####################     While Loops     #####################
##############################################################
print("******************  while loop  ************")
#  Form
#   while condition=true:
#       do something

#  set iteration variable
n=5

while n>0:
    print(n)
    #  change iteration variable
    n=n-1

print('blast off!')
print(n)

#  Watch out for infinite loops!!!!
#  in example below iteration variable doesn't change (n>0 always)
# n=5
# while n>0:
#     print('lather')
#     print('rinse')
#     exit()
# print('dry off')


#  zero trip loop
n=0
while n>0:  #  never true
    print("in loop")
print("out of n=0 loop")

##############################################################
##################     Exiting Loops     #####################
##############################################################
print("")
print("******************  exit loops  ************")

#  Breaking out of a loop
while True:
    line=input('>')
    if line=="done":
        break # get's out of the
    print(line)
print("break loop done")

#  continue loop
while True:
    line=input('>')
    if line[0]=="#":
        continue # continue back to the top of loop once here
    if line == 'done':
        break
    print(line)
print('continue loop done')

#  The while loop is an indefinite loop

##############################################################
####################     For Loops     #######################
##############################################################
print("")
print("******************  for loops  ************")

#  For loops are definite loops

for i in [5,4,3,2,1]:
    print(i)
print('blast off!!!')

friends=['joe','glen','sally']

for friend in friends:
    print("happy new year: ",friend)
