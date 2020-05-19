def binarySearch1(searchFor, numbers = [], *args):
    maxRange = len(numbers) - 1
    minRange = 0
    while True:
        midpoint = int((maxRange + minRange)/2)
        if numbers[midpoint] < searchFor and numbers[midpoint + 1] >= searchFor:
            return len(numbers) - midpoint - 1
        if numbers[midpoint] < searchFor:
            minRange = midpoint + 1
        else:
            maxRange = midpoint - 1
   
        
input()
inputArray = list(map(int,input().split()))
#for i in range(0, len(inputArray)): 
#    inputArray[i] = int(inputArray[i]) 
inputArray.sort()
testCases = int(input())
for x in range(testCases):
    inputArray2 = input().split()
    if inputArray2[0] is '0':
        if int(inputArray[0]) >= int(inputArray2[1]):
            print(len(inputArray))
        elif int(inputArray[-1]) < int(inputArray2[1]):
            print(0)
        else:
            print(binarySearch1(int(inputArray2[1]), inputArray))
    else:
        if int(inputArray[0]) > int(inputArray2[1]):
            print(len(inputArray))
        elif int(inputArray[-1]) <= int(inputArray2[1]):
            print(0)
        else:
            print(binarySearch1(int(inputArray2[1]) + 1, inputArray))
        