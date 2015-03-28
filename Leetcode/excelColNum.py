"""
Excel column number lookup
A -> 1
B -> 2
...
Z ->26
AA -> 27
"""

import string,time

def titleToNum(t):
	t = t.upper() # in case lowercase
	col_num_dict = dict(zip(string.ascii_uppercase, range(1,27)))
	
	num =0
	for i, c in enumerate(t[::-1]):
		num +=(26**i) * col_num_dict.get(c) 
	return num


def titleToNum_v2(t): # one line without string module!
	return sum( 26**i * (int(c,36)-9) for i,c in enumerate(t[::-1]))


def test(algo, testcase):
	a =time.time()
	for t in testcase:
		print algo(t)
	b=time.time()
	print "time: ", b-a

# test 
testCase =["B", "AB", "BA", "BED"]

test(titleToNum, testCase)
test(titleToNum_v2, testCase)