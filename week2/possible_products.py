def possible_products(array):
    products = []
    for i in range(len(array)):
        for j in range(len(array)):
            products.append(array[i]*array[j])
    return products


input_numbers = input("Please input a group of number:")
input_numbers = input_numbers.split(' ')
array = []
for i in input_numbers:
    array.append(int(i))
products = possible_products(array)
print("Possible products:")
print(set(products))
