##############################################################
###########    Calculate Letter Grade from Test    ###########
##############################################################

score = input("Enter your test score points: ")

try:
    score=float(score)/100
except:
    print("Non numeric test score")
    exit()

if score >=0.9:
    grade="A"
elif score >=0.8:
    grade="B"
elif score >=0.7:
    grade="C"
elif score >=0.6:
    grade="D"
else:
    grade="F"

print("Grade = ",grade)
