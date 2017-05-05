##############################################################
###############    Temperature Conversion    #################
##############################################################

#  Ask user to input Temperature in Fahrenheit
F_Temp=float(input("Enter Temperature in Fahrenheit: "))
#  Convert Temperature to Celsius
C_Temp = (F_Temp-32.0)*5/9

print('Temperature in Celsius = ',C_Temp)
