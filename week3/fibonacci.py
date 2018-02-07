
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


num = int(input("Please input a number:"))
print("The {}th number in fibonacci series is : {}".format(num, fibonacci(num)))

