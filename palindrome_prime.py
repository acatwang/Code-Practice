"""
Challenge: return Biggest prime palindrome < 1000.
"""
def isPrime(num):
    if num<=3:
        return num==2
    if num%2==0 or num%3==0:
        return False
    for p in range(5, int(num**0.5)+1,6):
        if num%p==0 or num%(p+2)==0:
            return False
    return True
    
def isPalinmore(num):
    return num/100 == num%10

for i in range(1000):
    num = (1000-i)
    if isPrime(num) and isPalinmore(num):
        print num
        break