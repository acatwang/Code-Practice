"""
Challenge: Unique element in a list

"""
import sys
def main():
	#test_cases = open(sys.argv[1], 'r') # For CodeEval test
	test_cases = ["1,1,1,2,2,3,3,4,4","2,3,4,5,5"] # For local test
	for test in test_cases:
		unique = list(set([int(n) for n in test.split(',')]))
		print str(unique[0])+"".join([","+str(n) for n in unique[1:]])

if __name__ == "__main__":
	main()