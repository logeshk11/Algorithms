#finding a missing number in array

a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,44,45,46,47,48,49,50]
sum=sum(a)
total = (50*(51)/2)
print(f"{int(total-sum)} is the missing number")


#in a given array and a number return the indices of two number such that they add up to target

arr = list(map(int, input().split(' ')))
target=int(input())
print(arr)
print(target)
for i in range(len(arr)):
    for j in  range(i+1, len(arr)):
        if arr[i]==arr[j]:
            continue
        elif arr[i]+arr[j] == target:
            print(f"The index are {i} and {j}")



#remove duplicates

def removeDuplicates(myList):
    a = []
    for i in myList:
        if i not in a:
            a.append(i)
    return a

