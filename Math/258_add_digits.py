def addDigits(num):
    while num >= 10:
        s = 0
        while num > 0:
            s += num % 10
            num //= 10
        num = s
    return num

print(addDigits(129))
