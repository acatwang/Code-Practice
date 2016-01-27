"""
Word permutation
Given a word, print out all combination of that word
Example:
input - dog
output - dog, gdo, ogd,god,odg,dgo
"""
def permute(word,comb="",capital=False):
	#print 'word', word, 'comb:',comb
	word=word.lower()
	n = len(word)
	if n ==0:
		print comb

	for i,s in enumerate(word):
		#print word[:i]+word[(i+1):]
		permute( word[:i]+word[(i+1):],comb+(s))
		if capital:
			permute( word[:i]+word[(i+1):],comb+(s.upper()))


#permute ('Ab')
permute ('dog')
