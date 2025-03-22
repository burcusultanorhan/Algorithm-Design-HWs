import math
import random

def partition (myArray):
    pivot = myArray[0]
    
    length = len(myArray)
    
    tempArray = [pivot] * length
    i=0
    j=length-1

    for x in range(length):
        if myArray[x] < pivot:
            tempArray[i] = myArray[x]
            i = i+1
        elif myArray[x] > pivot:
            tempArray[j] = myArray[x]
            j = j-1
    
    myArray.clear()
    
    for x in range(length):
        myArray.append(tempArray[x])
    
    return i

def findMedian(theArray, median):

    location = partition(theArray)

    if location == median-1:
        solution = theArray[location]
        print("Median value of the array is:", solution)
    
    elif location > median-1:
        
        findMedian(theArray[:location], median)

    else:

        findMedian(theArray[location+1:], median-location-1)
        
def maxPoints(theMap, aAxis, bAxis, aLoc, bLoc, sum):
    if (aAxis == aLoc) & (bAxis == bLoc):
        print("\nTotal max points: ", sum)
        return sum

    if (aAxis == aLoc):
        sum = sum + theMap[aLoc][bLoc+1]
        maxPoints(theMap, aAxis, bAxis, aLoc, bLoc+1, sum)
    
    elif(bAxis == bLoc):
        sum = sum + theMap[aLoc+1][bLoc]
        maxPoints(theMap, aAxis, bAxis, aLoc+1, bLoc, sum)

    else:
        if theMap[aLoc+1][bLoc] > theMap[aLoc][bLoc+1]:
            sum = sum + theMap[aLoc+1][bLoc]
            maxPoints(theMap, aAxis, bAxis, aLoc+1, bLoc, sum)
        
        else:
            sum = sum + theMap[aLoc][bLoc+1]
            maxPoints(theMap, aAxis, bAxis, aLoc, bLoc+1, sum)
    
    

axisA = random.randint(0,9)
axisB = random.randint(0,9)

map = [[0 for w in range(axisB)] for h in range(axisA)] 

for x in range(axisA):
    for y in range(axisB):
        map[x][y] = random.randint(0,100)

print("Input: n =", axisA)
print("Input m =", axisB)
print("Game map: \n")

for x in range(axisA):
    print(map[x])

initialSum = map[0][0]

maxPoints(map, axisA-1, axisB-1, 0, 0, initialSum)

print("\n\n")

A = [0] * 11

for x in range(11):
    A[x] = random.randint(0,100)

medArray = math.ceil(len(A)/2)

print("Array to be searched: \n")
print(A)
findMedian(A, medArray)