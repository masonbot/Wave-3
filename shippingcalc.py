def shiping(items):
    sum = 0
    for i in range(items + 1):
        if i == 1:
            sum += 10.95
        elif i > 1:
            sum += 2.95
    return sum

a = int(input("Input the number of items: "))
b = shiping(a)
print("You have to pay $" + str(round(b, 2)) + " in shipping fees")
