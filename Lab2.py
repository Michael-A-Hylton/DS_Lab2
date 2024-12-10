#2a
integerList=[]
i=0
while True:
    userInput=(input("integer to add to the list: "))
    integerList.append(userInput)
    if integerList[i] == "x":
        integerList.remove("x")
        break
    else:
        userInput=int(userInput)
    i+=1
#2b
for x in range(len(integerList)):
    integerList[x]=int(integerList[x])
    print(integerList[x])
    
j=0

while True:
    #2c
    listType=type(integerList[j])
    print("Data type of item %d: %s" % (j, listType) )
    j+=1
    if j > len(integerList)-1:
    #2d
        print("your length is: " + str(j))
        break

#2e
sumVal=0
maxVal=integerList[0]
minVal=integerList[0]
for x in range(1,len(integerList)):
    sumVal=sumVal+integerList[x]
    avgVal=sumVal/x
    if integerList[x] >= maxVal:
        maxVal=integerList[x]
    elif integerList[x] <= minVal:
        minVal=integerList[x]
#2f
print("Total sum: " + str(sumVal))
#2g
print("Average: " + str(avgVal))
#2h
userInput=int(input("Please give a number to see if it is in the list: "))
for x in range(len(integerList)):
    if integerList[x]==userInput:
        print("True")
        break
    elif x+1==len(integerList):
        print("False")
        break
    

#2i
x=0
while x<=(len(integerList)-1):
    y=x+1
    while y<=(len(integerList)-1):
        if integerList[x] > integerList[y]:
                tempVal=integerList[x]
                integerList[x]=integerList[y]
                integerList[y]=tempVal
        y+=1
    x+=1
x=0
print("Ordered List: ")
for x in range(len(integerList)):
    print(integerList[x])

#2j
for x in range(len(integerList)-1):
    if integerList[x] < integerList[x+1]:
        print("True")
    else:
        print("False")

#2k
freqDict={}
for x in range(len(integerList)):
    if integerList[x] in freqDict:
        freqDict[integerList[x]]+=1
    else:
        freqDict[integerList[x]]=1

print(freqDict)
