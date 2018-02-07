
def fibonacci(n):
    global count
    count = count+1
    print("Calling fibonacci at {}th, n = {}".format(count, n))
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


count = 0
num = int(input("Please input a number:"))
print("The {}th number in fibonacci series is : {}".format(num, fibonacci(num)))

