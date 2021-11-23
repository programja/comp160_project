import random
import time
from array import array

# Random list generator from input numbers. Fairly basic.
def randomlist(howmany, start, stop):
    randomlist = list()
    for i in range(howmany):
        randint = random.randrange(start,stop)
        randomlist.append(randint)
    return randomlist

# Will start with COUNTINGSORT
def csort(inputlist):

    # Find the largest element in the input list
    # This will determine how large to make 'counting' list
    largest = 0
    for i in range(len(inputlist)):
        if inputlist[i] > largest:
            largest = inputlist[i]

    # Initialize the input list for output and count/cumulative lists
    # Also the counting list to add to output
    outputlist = list(inputlist)
    countcumlist = list()
    countlist = list()
    cumlist = list()

    # Fill cumulative list with 0's
    for i in range(largest):
        countcumlist.append(0)
        countlist.append(0)
        cumlist.append(0)

    # Fill the counting list with, uhm, counts
    for j in range(0, len(inputlist)):
        countcumlist[inputlist[j]-1] += 1
        countlist[inputlist[j]-1] += 1
        cumlist[inputlist[j]-1] += 1

    # Create the cumulative list
    for x in range(1, largest):
        countcumlist[x] += countcumlist[x-1]
        cumlist[x] += cumlist[x-1]

    # Create the brand new sorted list
    # The in range is stepping through the input list
    # len(inputlist) -1, is the start, -1 is the stop, -1 is the incremental steps
    # This is starting from the end of the input list and
    # using each value, finding it's index in the output list and
    # decrementing that cumulative count by 1
    for z in range(len(inputlist)-1,-1,-1):
        outputlist[countcumlist[inputlist[z]-1]-1] = inputlist[z]
        countcumlist[inputlist[z]-1] -= 1

    # Return the sorted output list
    return outputlist, countlist, cumlist

def modcsort(proclist, place):
    #Find length of list, per values in place
    length = len(proclist)

    # Create output/sorted list
    outputlist = [0] * length
    # Create temp count list
    countlist = [0] * (10)

    # Store counts of occurrences based on place given
    for i in range(0,length):
        walkindex = proclist[i] // place
        countlist[walkindex % 10] += 1

    # Another cumulative list, index positions bruh
    for j in range(1,10):
        countlist[j] += countlist[j-1]

    # Finishing up by putting together the output
    x = length - 1
    while x >= 0:
        walkindextwo = proclist[x] // place
        outputlist[countlist[walkindextwo % 10] - 1] = proclist[x]
        countlist[walkindextwo % 10] -= 1
        x -= 1

    # Copying over the sorted values or tossing away temp output
    z = 0
    for z in range(0, len(proclist)):
        proclist[z] = outputlist[z]

def rsort(inputlist):

    # Find the max of our inputlist (places people, places)
    biggestnumber = max(inputlist)

    # COUNT SORT those digits
    # For clarity, we start at the ones place, and iterate to the 10's place
    # We do this by raising our current place value by 10^place
    # This gives us: 1's place, 10's place, 100's place until done (max)
    place = 1
    while biggestnumber / place > 0:
        modcsort(inputlist, place)
        place *= 10

    outputlist = inputlist
    return outputlist



print("Welcome to RADIXSORT you big goofball.")
time.sleep(1.0)
print("Let's begin the test.")
time.sleep(1.0)
print("Generating an input list.")
time.sleep(1.0)
inputlist = randomlist(50,200,300)

radixoutputlist = rsort(inputlist)

print("Radix input list: ", inputlist)
print("Radix output list: ", radixoutputlist)










# USER INTERACTION PROCESSES

#
# inputlist = list()
# yes = "Y"
# no = "N"
#
# print("Welcome to COUNTINGSORT, we're glad you're here.")
# time.sleep(1.0)
# print("As usual some basic rules: ")
# time.sleep(1.0)
# print("No negative integers and the more cluster-y or repeating the better.")
# time.sleep(1.0)
# print("This is COUNTINGSORT so, yeah, you'll do fine.")
# time.sleep(1.0)
# randorno = input("Type 'Y' to create your own input or 'N' to run a prebuilt list: ")
# time.sleep(1.0)
#
# if randorno == yes:
#     print("Give me a total # of values, start and stop and we can randomize the rest.")
#     time.sleep(1.0)
#     howmany = int(input("How many values do you want?: "))
#     time.sleep(0.5)
#     print("That many? Really? OK, ok we'll see what we can do.")
#     time.sleep(0.5)
#     start = int(input("What is the starting value you want?: "))
#     time.sleep(0.5)
#     print("Just kidding, we can handle this. Little computer science joke.")
#     time.sleep(0.5)
#     stop = int(input("What value would you like to end with?: "))
#     time.sleep(0.5)
#     print("Got it. Give me a second.")
#
#     inputlist = randomlist(howmany,start,stop)
#
# elif randorno == no:
#     print("Got it, using a pre-built list.")
#
#     inputlist = randomlist(30,1,10)
#
# else:
#     print("That is not a valid choice. You know this, don't be weird.")
#
# time.sleep(3.0)
# print("Running COUNTINGSORT now. Should take at most O(n+k) time.")
# time.sleep(1.0)
# print(" . . . . ")
# time.sleep(1.0)
#
# output = csort(inputlist)
#
# print("Input list: ", inputlist)
# print("Intermediary count list: ", output[1])
# print("Intermediary cumulative list: ", output[2])
# print("Sorted output list: ", output[0])
