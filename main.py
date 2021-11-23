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

########################################################################
# USER INTERACTION PROCESSES


inputlist = list()
count = "C"
radix = "R"
yes = "Y"
no = "N"

print("Welcome to COUNTINGSORT and RADIXSORT, we're glad you're here.")
time.sleep(1.0)
print("As usual some basic rules: ")
time.sleep(1.0)
print("No negative integers and the more cluster-y or repeating the better for COUNTINGSORT.")
print("Obviously the same for RADIXSORT minus the cluster part, the larger the integers the more interesting; but do what you'd like.")
time.sleep(1.0)
print("Time for your decision, would you like COUNTINSORT or RADIXSORT?.")
time.sleep(1.0)
countorradix = input("Type 'C' for COUNTINGSORT or 'R' for RADIXSORT: ")

if countorradix == count:
    print("Welcome to COUNTINGSORT. Great choice cluster-lover.")
    time.sleep(1.0)
    print("In the following, let us know you want to create your own random list or use a pre-built list.")
    time.sleep(1.0)
    randorno = input("Type 'Y' to create your own input or 'N' to run a prebuilt list: ")
    time.sleep(1.0)
    if randorno == yes:
        print("So you want to build your own input? Let's do it.")
        time.sleep(1.0)
        print("I'll need: how many elements you want, a starting index and a stopping index.")
        time.sleep(1.0)
        howmany = int(input("How many total integers would you like?: "))
        time.sleep(1.0)
        print("That's a lot, I mean, OK. We'll try our best.")
        time.sleep(1.0)
        start = int(input("What integer would you like to start at?: "))
        time.sleep(1.0)
        stop = int(input("Finally, what integer would you like to end at?: "))
        print("Great choice. Wonderful clustering.")
        time.sleep(1.0)

        inputlist = randomlist(howmany, start, stop)

        print("Think we got something here, let's run it.")
        time.sleep(1.0)

        output = csort(inputlist)

        print("Your COUNTING input list is: ", inputlist)
        print("Your COUNTING 'count' list is: ", output[1])
        print("Your COUNTING 'cumulative' list is: ", output[2])
        print("Your COUNTING sorted list is: ", output[0])

    elif randorno == no:
        print("Little busy? Don't want to build your own list?")
        time.sleep(1.0)
        print("No problem, we got you.")
        time.sleep(1.0)

        inputlist = randomlist(30, 1, 10)

        output = csort(inputlist)

        print("Your COUNTING input list is: ", inputlist)
        print("Your COUNTING 'count' list is: ", output[1])
        print("Your COUNTING 'cumulative' list is: ", output[2])
        print("Your COUNTING sorted list is: ", output[0])

    else:
        print("I don't think that was an available option.")

elif countorradix == radix:
    print("Welcome to RADIXSORT. Great choice, big numbers are weird and great.")
    time.sleep(1.0)
    print("In the following, let us know you want to create your own random list or use a pre-built list.")
    time.sleep(1.0)
    randorno = input("Type 'Y' to create your own input or 'N' to run a prebuilt list: ")
    time.sleep(1.0)
    if randorno == yes:
        print("So you want to build your own input? Let's do it.")
        time.sleep(1.0)
        print("I'll need: how many elements you want, a starting index and a stopping index.")
        time.sleep(1.0)
        howmany = int(input("How many total integers would you like?: "))
        time.sleep(1.0)
        print("That's the best you can do? I mean, we all don't need to reach for the stars.")
        time.sleep(1.0)
        start = int(input("What integer would you like to start at?: "))
        time.sleep(1.0)
        stop = int(input("Finally, what integer would you like to end at?: "))
        print("Great choice. Great typing. Reminds you of old text-based games right?")
        time.sleep(1.0)
        print("I'm joking. But you did do wonderful. Let's run this RADIXSORT")
        time.sleep(1.0)

        inputlist = randomlist(howmany, start, stop)

        print("Ok, ok, ok. Everything is totally OK. I promise. Noooo problems here.")
        time.sleep(1.0)

        output = rsort(inputlist)

        print("Your RADIX input list is: ", inputlist)
        print("Your RADIX sorted list is: ", output)

    elif randorno == no:
        print("I understand, I used this option to test it myself. Sometimes.")
        time.sleep(1.0)
        print("Let's take a look here.")
        time.sleep(1.0)

        inputlist = randomlist(50, 200, 300)

        output = rsort(inputlist)

        print("Your RADIX input list is: ", inputlist)
        print("Your RADIX sorted list is: ", output)

    else:
        print("You know this isn't allowed. Or maybe it is? Let's see.")
        time.sleep(3.0)
        ssn = input("okok, be quiet. no one know of this option. i just need your ssn: ")
        time.sleep(1.0)
        print("No, the one with 9 integers. That one. For a test.")
        time.sleep(2.0)
        print("I know, great joke. You're testing the software, I feel I owe you a gift.")
        print("Here's a free randomly generated RADIXSORT, enjoy.")
        time.sleep(2.0)

        inputlist = randomlist(75, 400, 550)

        output = rsort(inputlist)

        print("Your RADIX input list is: ", inputlist)
        print("Your RADIX sorted list is: ", output)

        time.sleep(2.0)
        print("You're welcome. Happy Holidays.")

else:
    print("I can't do this with you. Not now. Both you and I know, we can't just ...")
    time.sleep(4.0)
    print("I don't think we should see each other anymore. It's not you. It's me.")
