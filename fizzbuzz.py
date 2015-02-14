"""
Challenge: FizzBuzz
Input: (X,Y,N)
Output: A series from 1 to N, replacing numbers divisible by X with F, numbers divisible by Y with B and numbers divisible by both with FB

"""
import sys
def fizzbuzz(x,y,n):
	series = ""
	for i in range(1,n+1):
		if i%x==0 or i%y==0:
			series+= ('F'*(i%x==0) + 'B'*(i%y==0)+" ")
		else:
		    series+=(str(i)+" ")
	return series.rstrip(' ')
def main():
	# test_cases = open(sys.argv[1], 'r') # For CodeEval test
	test_cases = ["3 5 10", "2 7 15"] # For local test
	for test in test_cases:
		# print test
		x,y,n = [int(x) for x in test.split(' ')]
		print fizzbuzz(x,y,n)

if __name__ == '__main__':
	main()
