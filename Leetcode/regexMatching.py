"""
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Recursive
Takes 57ms
"""
cache={}
# @return a boolean
def isMatch(s, p):	
	# Store result in dict to save some times
	if (s,p) in cache:
		return cache.get((s,p))

	#print s," | ",p
	# with no *
	if "*" not in p and "." not in p:
		return s==p

	if p[-1] == "*":
		# Match zero
		if isMatch(s,p[:-2]):
			cache[(s, p)] = True
			return True

		# Match One
		if s!="" and (s[-1]==p[-2] or p[-2]==".") and isMatch(s[:-1],p[:-2]):
			cache[(s,p)] = True
			return True

		# Match multiple
		if s!="" and (s[-1]==p[-2] or p[-2]==".") and isMatch(s[:-1],p):
			cache[(s,p)] = True
			return True

		cache[(s,p)] = False

	if s=="":
		return p==""
			
	if p[-1] == s[-1] or p[-1]==".":
		if len(s)>1:
			return isMatch(s[:-1],p[:-1])
		elif len(s)==1 and len(p)>1:
			#return True
			return isMatch("",p[:-1])
		else:
			#return isMatch("",p[:-1])
			#cache[(s,p)] = True
			return True
	else:
		#cache[(s,p)] = False
		return False

# print isMatch("aa","a")
# print isMatch("aa","aa")
# print isMatch("aaa","aa")
# print isMatch("aa", "a*")
# print isMatch("aa", ".*")
# print isMatch("aab", "c*a*b")
# print isMatch("aaa", "ab*ac*a")
# print isMatch("a", ".*..a*")
# print isMatch("a", "ab*a")
# print isMatch("", "..ac")
# print isMatch("aaca", "ab*a*c*a")
# print isMatch("ab", ".*c")
#print isMatch("aaa", ".*")
# print isMatch("aaa", ".a")
# print isMatch("a", "ab*a")
# print isMatch("aasdfasdfasdfasdfas", "aasdf.*asdf.*asdf.*asdf.*s")
print isMatch("caacacabbbaaccba", "b*b..*b*.*c*.*a*")