##############################################################
###################    Smallest Value    #####################
##############################################################

print("Before")
smallest_so_far = None

#  loop through an
for value in [9,41,12,3,74,15]:
    if smallest_so_far is None:
        smallest_so_far = value
    if value < smallest_so_far:
        smallest_so_far = value
    print("smallest_so_far =",smallest_so_far,"array_val =",value)

print("After")
print("smallest_val =",smallest_so_far)

print("")
print("Before")
largest_so_far = -1

#  loop through an array
for thing in [9,41,12,3,74,15]:
    print(thing)
    if thing>largest_so_far:
        largest_so_far = thing
print("After")
print("largest_so_far = ",largest_so_far)
