def fibonacci_iterative(n):
    acc1 = 1
    acc2 = 1
    acc3 = 1
    for i in range(2, n):
        acc3 = acc1 + acc2
        acc1, acc2 = acc2, acc3
    return acc3
num = int(input("Please input a number:"))
print("The {}th number in fibonacci series is : {}".format(num, fibonacci_iterative(num)))
