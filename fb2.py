def countdown(start):
# Starting an empty list to hold the countdown
    cd = []
# Going through the countdown starting at the given int going back to 0 by 1
    for x in range(start,-1,-1):
# Every time it loops it add the new x to the premade list
        cd.append(x)
    return(cd)

print(countdown(5))



def printAndReturn(list):
        print (list[0])
        return list[1]

print(printAndReturn([1,2]))



def firstPlusLength(list):
    return list[0] + len(list)

print(firstPlusLength([1,2,3,4,5]))



def valuesGreaterThanSecond(list):
# Setting an empty list to store which ints are larger than the 2nd int
# Also keeping a count of how many are larger
    newList = []
    count = 0
    for x in list:
# Checking each index to see if its bigger than index 1 (The second number)
        if x > list[1]:
# If it finds one the count goes up by one and the number gets added to the new list
            count += 1
            newList.append(x)
    print(count)
    return newList

print(valuesGreaterThanSecond([5,2,3,2,1,4]))



def lengthAndValue(x,y):
# Creating a new list
    newList = []
    for z in range(x):
# starts from to and goes till the x var, each time it goes through the loop it adds one of the y to the list
        newList.append(y)
    return newList

print(lengthAndValue(4,7))
print(lengthAndValue(6,2))