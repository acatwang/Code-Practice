"""
Write a program that prints (to STDOUT) the numbers from 1 to 100. 
But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
For numbers which are multiples of both three and five print "FizzBuzz".
"""

# v1
for i in range(1,101):
    s = "Fizz"*(i%3==0)+"Buzz"*(i%5==0)
    print i if s=="" else s

# v2: shorter code
for i in range(1,101):print "Fizz"*(i%3==0)+"Buzz"*(i%5==0) or i

# v2.2: even shorter
for i in range(100):print "Fizz"*(i%3/2)+"Buzz"*(i%5/4) or i+1
