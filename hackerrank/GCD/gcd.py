
def divide(g,a):
    if a==0:
        return g
    else:
        return divide(a,g%a)
        
T = int(raw_input())
     
for _ in range(T):
    N = int(raw_input())
    A = [int(x) for x in raw_input().split(" ")]
    gcd=A[0]
    for i in xrange(1,N):
        gcd =divide(gcd,A[i])

    print "YES" if gcd==1 else "NO"