"""
Given a string S, find the longest palindromic substring in S. 
Assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
"""

# Dynamic Programming : keep a table of palindromic
# Runtime: quadratic
# Space: quadratic
def longestPalidrome(s):
	N = len(s)
	table = dict(((i,j),False) for i in range(N) for j in range(N))
	longestLen = 1
	startIdx = 0
	for i in range(N):
		table[(i,i)] = True

	for i in range(N-1):
		if s[i] == s[i+1]:
			table[(i,i+1)] = s[i]==s[i+1]
			longestLen=2

	for size in range(2,N):
		for i in range(N-size):
			j = i+size
			if s[i]==s[j] and table[(i+1,j-1)]:
				table[(i,j)] = True
				longestLen = size
				startIdx = i

	return s[startIdx:startIdx+longestLen+1]

print longestPalidrome('aba')
print longestPalidrome('cabacdgfdcaba')

# Expand from center
# Runtime: quadratic
# Space: constant
def expandFromCenter(s,i,j):
	left =i
	right=j
	while left>0 and right<len(s) and s[left] == s[right]:
		left -=1
		right +=1
	return s[left:right+1], right-left
def longestPalidrome2(s):
	N = len(s)
	longestLen = 1
	ans=s[0]

	if N==0:
		return ""

	for i in range(N-1):
		p1, len1 = expandFromCenter(s,i,i)
		p2, len2 = expandFromCenter(s,i,i+1)
		if len1>longestLen or len2>longestLen:
			longestLen = max(len1,len2)
			ans = p1 if len1>len2 else p2
	return ans
print longestPalidrome('aba')
print longestPalidrome2('cabacdgfdcaba')

