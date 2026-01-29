def isHappy(n):
    def getNext(num):
        total = 0
        while n > 0:
            digit = num % 10
            total += digit ** 2
            num //= 10
        return total
    
    
