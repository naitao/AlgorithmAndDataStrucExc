
def sortList(array):
    for i in range(len(array)):
       for j in range(i, len(array)): 
           if array[j] < array[i]:
               temp = array[i]
               array[i] = array[j]
               array[j] = temp
    return array

def binarySearch(myarray, elem):
    low = 0
    high = len(myarray)-1
    
    while (low < high):
        mid = int((low+high)/2)
        if elem <= myarray[mid]:
            high = mid
        else:
            low = mid + 1
        if low == high:
            return low   

input_numbers = input("Please input a group of number:")
input_numbers = input_numbers.split(' ')
array = []
for i in input_numbers:
    array.append(int(i))
newArray = sortList(array)
print(newArray)
elem = int(input("please input the searching number:"))
print("The location of this number is {}".format(binarySearch(newArray, elem)))
