n = int(input("Enter an integer(2 or greater): "))
factor = 2
while n <= 2:
    n = int(input("Enter an integer(2 or greater): "))
print("The factors of", n, "are: ")
while factor <= n :
    if n % factor == 0:
        print(factor)
        n //= factor
    else:
        factor +=1