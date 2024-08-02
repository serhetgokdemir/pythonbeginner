def primeCheck(number):
    isPrime = True
    for i in range(2,number):
        if (number%i == 0):
            isPrime = False
            break
    return isPrime


if __name__ == "__main__":
    while True:
        number = int(input("Enter the #: "))
        print(primeCheck(number))
        if number == 0: break
