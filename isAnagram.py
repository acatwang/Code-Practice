
#Given two string return whether they are isAnagram
def isAnagram(s1,s2):
	s1 = sorted(s1)
	s2 = sorted(s2)

	return s1==s2

print isAnagram('abcde','edcba')
print isAnagram('abcde','edcioa')

# Given a list of strings, group the anagrams
def groupAnagram(s_list):
	anagrams = {}
	for s in s_list:
		ana = "".join(sorted(s))

		if ana in anagrams:
			anagrams[ana].append(s)
		else:
			anagrams[ana] = [s]
	return anagrams

print groupAnagram(['abcde','edcba','mary','army','mars','arms','march','charm'])
