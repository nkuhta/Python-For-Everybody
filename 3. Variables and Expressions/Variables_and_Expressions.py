##################################################
##############  Variable assignment  #############
##################################################
#  section label
print("******************************  Variable Assignment   ***************")

#  assign the value 12 to variable a
a=12
#  now add 2 to a (so now a=14)
a=a+2
#  print out the current value of a+2
print("a+2 =",a+2)

#  more complicated assignment operator
x=3.9*a*(1-a)
print("x =",x)

##################################################
############  Numeric Operators  #################
##################################################
#  section label
print("******************************   Numeric Operators   ***************")

    #   +   = Addition
    #   -   = Subtraction
    #   *   = Multiplication
    #   /   = Division
    #   **  = Power
    #   %   = Remainder

#  Addition/Subtraction
xx = 2
xx = xx + 2
print("xx =",xx)
print("xx-2 =",xx-2)

#  Multiplication/Division
yy=440*12
print('yy =',yy)
zz=yy/1000
print('zz =',zz)

#  Remainder
jj=23
kk=jj % 5
print("23/5 Remainder = ",kk)

#  Power
print("4^3 = ",4**3)

#   Order of Operations
#   1.  Parenthesis
#   2.  Power
#   3.  Multiplication (and Division)
#   4.  Addition (and Subtraction)
#   5.  Left to Right

##################################################
##################    Types    ###################
##################################################
#  section label
print("******************************   Types   ***************")


#  integer, float, character string

#  string concatination (note the space)
eee="hello "+"there"
print(eee)

#  incompatible type combination (traceback error)
#   eee=eee+1

#  type function
str_type=type(eee)
int_type=type(1)
float_type=type(1.0)

print(str_type,int_type,float_type)

#  force float type conversion
print(type(99),type(float(99)))

#  String conversion
sval='123'
print(int(sval)+1)
#  This below won't work because
#print(sval+1)

##################################################
###############    User Input    #################
##################################################
#  section label
print("******************************   User Input   ***************")

#  run program in command line to use input
# input("") is asking for user Input string
nam=input("who are you?")
print('welcome',nam)
input("press enter to continue")

#  converting user input (add 1 to European floor to get US floor)
inp = input("Europe floor?")
usf = int(inp) + 1
print("US floor",usf)
input('press enter to continue')

#  name variables such that they make sense
Hours=float(input("Enter Hours:"))
Pay_Rate=float(input("Rate of Pay:"))
total_pay=Pay_Rate*Hours
print("Total Payout =",total_pay)
input('press enter to continue')
