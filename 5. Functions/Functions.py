##############################################################
##################    Function Basics    #####################
##############################################################

# def = define function command
def hello():
    print('hello')
    print('fun')

# call hello function
hello()
print('zip')
# call hello function again
hello()
print('***********')
#  Built-in function max
big=max('Hello world')
print("highest character in string: ",big)

tiny=min('Hello world')
print("smallest character in string: ",tiny)

#  Functions have IPO (Input,Processing,Output)

##############################################################
###############    Built-in Functions    #####################
##############################################################
print("")
print("******************  Built-in Functions  ************")

# Type conversions (float,type,str,int)
print(float(99/100))
print(type(42))

#  String conversions
sval="123"
sval=int(sval)
print("sva1+1 = ",sval+1)

##############################################################
###############    Built our own Functions    ################
##############################################################
print("")
print("******************  Build our own Functions  ************")

x=5
print('hello')

#  note defining a function does not execute it
def print_lyrics():
    print("I'm okay")
    print("I sleep all night")

print("yo")
print_lyrics()
x=x+2
print(x)

##############################################################
#################    Function Parameters    ##################
##############################################################
print("")
print("******************  Function Parameters  ************")

def greet(lang):
    if lang == "es":
        print('Hola')
    elif lang == "fr":
        print("Bonjour")
    else:
        print("Hello")

greet("en")
greet("es")
greet("fr")

##############################################################
####################    Return Values    #####################
##############################################################
print("")
print("******************  Return Values  ************")

def greet():
    return "Hello"

print(greet(),"Glenn")
print(greet(),"Sally")

#  rewrite greet function with return commands.
def greet(lang):
    if lang == "es":
        return 'Hola'
    elif lang == "fr":
        return "Bonjour"
    else:
        return "Hello"

print(greet('en'), 'Glenn')
print(greet('es'), 'Sally')
print(greet('fr'), 'Mike')

#  Squared number function
def sq(xx):
    return xx**2

print(sq(2))

##############################################################
################    Multiple Parameters    ###################
##############################################################
print("")
print("******************  Multiple Parameters  ************")

def addtwo(a,b):
    added=a+b
    return added    

x=addtwo(3,5)
print(x)
