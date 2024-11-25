number = 29
isPrime = True

if number > 1:
    for i in range(2, number - 1):
        if (number%i) == 0:
            isPrime = False
            break
if isPrime:
    print(number, "is Prime")
else:
    print(number, "is not Prime")