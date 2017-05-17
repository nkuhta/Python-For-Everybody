
##############################################################
##############    Add, Count, and Average    #################
##############################################################


def ACA():

    sum_so_far=0
    average=0
    count=0

    while True:
        #  user inputs a numeric string
        number_str = input("Enter a number: ")

        #  once user types done, break
        if number_str == 'done':
            break
        #  exception handling to make sure the input is float
        try:
            float(number_str)
            count=count+1
            sum_so_far = sum_so_far + float(number_str)
        except:
            print("not a floating point number")

        sum_total = sum_so_far
        average = sum_total/count

    print("average =",average)
    print("sum =",sum_total)
    print("count =",count)

#  call the def Add/Count/Average ACA function
ACA()
