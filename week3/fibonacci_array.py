def fibonacci_array(my_array):
    if len(my_array) == 1 or len(my_array) == 2:
        return 1
    else:
        my_array[0] = 1
        my_array[1] = 1
        for i in range(2, len(my_array)):
            my_array[i] = my_array[i-1] + my_array[i-2]
        return my_array[-1]

num = int(input("Please input a number:"))
my_array = [0] * num
print("The {}th number in fibonacci series is : {}".format(num, fibonacci_array(my_array)))



