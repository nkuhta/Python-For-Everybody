##############################################################
#################    Boolean Statements    ###################
##############################################################

Boo_1 = 5==5
print(Boo_1)

Boo_0 = 5==6
print(Boo_0)

print(type(Boo_0),type(Boo_1))

##############################################################
###############    If Statement Structure    #################
##############################################################
print("********************  Nested If Section   **********")
#  Nested If Statement
x = 42
print("x = ",x)
if x>1:
    print('x > 1')
    #  nested (tabbed) if Statement
    if  x<100:
        print("x < 100")
print("Nested If Done")

##############################################################
#################    If/Else Statements    ###################
##############################################################
print("********************  If/Else Section   **********")

x = 4
print("x = ",x)

if x>2:
    print("Bigger than 2")
else:
    print("Smaller than 2")
print("If/Else Done")

#  multi-level if/Else

if x<2:
    print("Small")
elif x<10:
    print("Medium")
else:
    print("Large")
print("elif done")

#  note you don't need an else, and you can have many elif Statements

#  is x even or odd?

if x%2 == 0:
    print("x is Even")
else:
    print("x is Odd")

##############################################################
###############    Try/Except Conditionals    ################
##############################################################
print("********************  Try/Except Section   **********")
astr = "Hello Bob"

#  try to make str into int, use except if traceback problem
try:
    istr = int(astr)
except:
    istr = -1

print("First",istr)

#  Now try the same with a numerical string
astr="123"

try:
    istr=int(astr)
except:
    istr=-1

print("Second",istr)

#  try to have as little as possible in the try block to identify what's failing

#  Sample Try/Except with user input

rawstr=input('Enter a number: ')

try:
    ival=int(rawstr)
except:
    ival="nan"

if ival == "nan":
    print("Not a number")
else:
    print("Nice work")
