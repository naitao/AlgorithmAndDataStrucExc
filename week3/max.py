def max(my_array, index):
    if index == len(my_array)-1:
        return my_array[index-1]
    else:
        bigNum = max(my_array, index+1)
        return my_array[index] if my_array[index] > bigNum else bigNum

input_numbers = input("Please input a group of number:")
input_numbers = input_numbers.split(' ')
array = []
for i in input_numbers:
    array.append(int(i))
maxNum = max(array, 0)
print("The max number is:", maxNum)


