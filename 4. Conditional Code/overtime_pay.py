##############################################################
###########    Calculate Pay including overtime    ###########
##############################################################


hours=input("Enter Number of Hours: ")

try:
    hours=float(hours)
except:
    print(" please try again: hours needs to be a numeric value")
    exit()

payrate=input("Enter payrate ($/hour): ")

try:
    payrate=float(payrate)
except:
    print(" please try again: payrate needs to be a numerical value. ")
    exit()

if hours <= 40:
    #  when there is no overtime
    money = hours*payrate
else:
    #  40 hour money + overtime at 1.5x the payrate
    money = 40*payrate+1.5*payrate*(hours-40)

print("paycheck = ",money)
