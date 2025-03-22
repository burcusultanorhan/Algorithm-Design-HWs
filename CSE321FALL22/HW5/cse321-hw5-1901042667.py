import random


def longestCommonSubstring(myStringArray, bottom, top):

    if top == bottom:
        return myStringArray[top]
    
    if top > bottom:
        middle = bottom + (top-bottom)//2

    substring1 = longestCommonSubstring(myStringArray, bottom, middle)
    substring2 = longestCommonSubstring(myStringArray, middle+1, top)

    length1 = len(substring1)
    length2 = len(substring2)

    if length1 > length2:
        length1 = length2

    buildString = ""
    i = 0

    while i < length1:
        if substring1[i] != substring2[i]:
            break
        buildString = buildString + substring1[i]
        i = i+1
    
    return buildString



def maximizeProfitDQ(thisArray):
    
    if len(thisArray) <= 1:
        return 0;


    leftArray  = thisArray[:len(thisArray) // 2]
    rightArray = thisArray[len(thisArray) // 2:]


    bestOfLeft  = maximizeProfitDQ(leftArray)
    bestOfRight = maximizeProfitDQ(rightArray)
    bestOfBoth = max(rightArray) - min(leftArray)
    best = max(bestOfLeft, bestOfRight, bestOfBoth)

    return best



def maximizeProfit(thisArray2):

    min = thisArray2[0]
    tempMin = thisArray2[0]
    gap = 0

    for i in range(1,len(thisArray2)):
        tempGap = thisArray2[i] - tempMin

        if(tempGap > gap):
            gap = tempGap

        elif (thisArray2[i] < min):
            tempMin = thisArray2[i]

    return gap



def longestIncreasingSubarray(myArray):

    maxSubarray = 0
    length = len(myArray)
    dynamicValues = [1] * length

    for i in range(0,length):

        j = i-1 

        if myArray[j] < myArray[i]:
            dynamicValues[i] = max(dynamicValues[i], dynamicValues[j]+1)
    
        maxSubarray = max(maxSubarray, dynamicValues[i])
                    
    return maxSubarray



def maxPointsDynamic(theMap, aAxis, bAxis):
    
    dynamicPoint = theMap[0][0]
    i=0
    j=0

    for x in range(aAxis + bAxis):

            if (i == aAxis & j == bAxis):
                break

            elif i == aAxis:
                dynamicPoint = dynamicPoint + theMap[i][j+1]
                j = j+1
            
            elif j == bAxis:
                dynamicPoint = dynamicPoint + theMap[i+1][j]
                i = i+1
            
            else:
                dynamicPoint = dynamicPoint + max(theMap[i+1][j], theMap[i][j+1])
                if max(theMap[i+1][j], theMap[i][j+1]) == theMap[i+1][j]:
                    i = i+1
                else:
                    j = j+1

    return dynamicPoint



def maxPointsGreedy(theMap, aAxis, bAxis):
    
    sum = theMap[0][0]
    
    aLoc = 0
    bLoc = 0
    
    for x in range (aAxis + bAxis):
        
        if aLoc == aAxis:
            bLoc += 1
        
        elif bLoc == bAxis:
            aLoc += 1
        
        else:
            if theMap[aLoc+1][bLoc] > theMap[aLoc][bLoc+1]:
                aLoc += 1
            else:
                bLoc += 1
        
        sum += theMap[aLoc][bLoc]

    return sum



theArray1 = ["burcu", "burcusultan", "burcusultanorhan", "burciga"]
length1 = len(theArray1)
answer1 = longestCommonSubstring(theArray1, 0, length1 - 1)
print(theArray1)
print("Longest common substring: " + answer1) 
print("\n")


size = 8

theArray2 = [0] * size

for x in range(size):
    theArray2[x] = random.randint(0,20)

print(theArray2)


answer2 = maximizeProfitDQ(theArray2)
print("Maximum profit found with Dynamic Programming: ",answer2)
answer2 = maximizeProfit(theArray2)
print("Maximum profit found without Dynamic Programming: ",answer2)
answer3 = longestIncreasingSubarray(theArray2)
print("Longest increasing subarray: ",answer3)

print("\n")

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

answer4 = maxPointsDynamic(map, axisA-1, axisB-1)
print("Max points found with Dynamic Programming: ",answer4)

answer4 = maxPointsGreedy(map, axisA-1, axisB-1)
print("Max points found with Greedy algorithm: ",answer4)