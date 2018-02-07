def reverse(my_array, index):
    if index == int(len(my_array)/2):
        return
    else:
        temp = my_array[index]
        my_array[index] = my_array[-(index+1)]
        my_array[-(index+1)] = temp
        reverse(my_array, index+1)

array = input("Please input a series elements:")
array = array.split(' ')
reverse(array, 0)
print(array)

