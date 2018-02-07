def max(my_array):
    # If the original list (my_array[]) only has one element, return it directly
    if len(my_array) == 1:
        return my_array
    # If the original list (my_array) has more than 2 elements, do the following steps:
    # 1. Get the shorter list (cut off the first element of original list my_array[])
    #    by calling recursion function, we call the new list as new_array
    # 2. Compare the first element of original list (my_array[]) with the first
    #    element of new list(new_array[]), insert the first element of original list
    #    to the appropriate positon in new_array[]
    # 3. Return new_array[]
    else:
        new_array = max(my_array[1:])

        if new_array[0] < my_array[0]:
            new_array.insert(0, my_array[0])
        else:
            new_array.insert(1, my_array[0])
        return new_array

input_numbers = input("Please input a group of number:")
input_numbers = input_numbers.split(' ')
array = []
for i in input_numbers:
    array.append(int(i))
new_array = max(array)
print("The max number is:", new_array)


