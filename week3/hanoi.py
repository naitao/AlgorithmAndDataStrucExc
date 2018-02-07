def hanoi(n, dock):
    if n == 1:
        return 1
    else:
        value1 = hanoi(n-1, dock)
        value2 = hanoi(n-1, dock)
        return (value1 + value2) + 1


num = int(input("Please input the lays number of Hanoi: "))
dock = {
	'A': [1,2, 999],
        'B': [999],
        'C': [999] 
       }
print("The steps you need to move on : {}".format(hanoi(num, dock)))
