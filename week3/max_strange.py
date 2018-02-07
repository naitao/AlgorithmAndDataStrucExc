def max(my_array):
    if len(my_array) == 1:
        return my_array
    else:
        new_array = max(my_array[1:])
        if new_array[0] < my_array[0]:
            new_array.insert(0, my_array[0])
        else:
            new_array.insert(1, my_array[0])
        return new_array
my_array = [1, 3, 5, 10, 23, 15]
print(max(my_array)[0])
