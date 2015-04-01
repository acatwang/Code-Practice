""" 
Longest common substring
find the longest string (or strings) that is a substring (or are substrings) of two or more strings.
"""

def lcs(s1,s2):
	
	m = len(s1)
	n = len(s2)

	substr = []
	cnt = 0
	table = dict(((i,j),0) for i in range(m+1) for j in range(n+1))
	print len(table)

	# create the table
	for i in range(m):
		for j in range(n):
			
			if s1[i] == s2[j]:
				#print 'indx: ', (i,j)
				table[(i+1,j+1)] = table[(i,j)] + 1
				cnt = max(cnt,table[(i+1,j+1)])
			else:
				table[(i+1,j+1)] = 0
	
	# find substring
	endIdx = 0
	subStrSize = 0
	i,j = m,n
	while i>0 and j>0:
		if table[(i,j)]>0 and table[(i,j)]>subStrSize:
			endIdx = i
			subStrSize = table[(i,j)]
			
		if table[(i-1,j)]>table[(i,j-1)]:
			i-=1
		else:
			j-=1


	print cnt
	print endIdx, subStrSize
	print s1[endIdx-subStrSize:endIdx]

lcs('abab','baba')
lcs('aabbb','aaaabc')
lcs('AGGTAB','GXTXAYB')