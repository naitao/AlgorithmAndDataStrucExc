
def fibonacci(n, acc1, acc2):
    if n == 1:
        return acc1
    elif n == 2:
        return acc2
    else:
        return fibonacci(n-1, acc2, acc2+acc1)


num = int(input("Please input a number:"))
print("The {}th number in fibonacci series is : {}".format(num, fibonacci(num, 1, 1)))

