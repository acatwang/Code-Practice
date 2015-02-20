"""
Sum of the first 1000 prime
"""

def isPrime(n):
    if n<=3:
        return n>=2
    if n%2 ==0 :
        return False
    if n%3 ==0:
        return False
    for denom in range(5,int(n**.5)+1,6):
        if n%denom ==0 or n%(denom+2)==0:
            return False

    return True

_sum=0
cnt=0
n=2
while cnt<1000:
    #print n
    if isPrime(n):
        #print cnt
        _sum+=n
        cnt+=1
    n+=1

print _sum