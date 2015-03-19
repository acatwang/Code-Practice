import timeit
class Solution(object):
	def minWindow(self,S, T):
		# len(T)<len(S)
		if len(set(T))> len(set(S)):
			return ""

		target={}
		for i,t in enumerate(T):
			if t not in target:
				target[t] = {'cnt':T.count(t),
							'indices':[i],
							'occur':0}
			else:
				target[t]['indices'].append(i)

		#print target
		pointers = dict((t_idx,-1) for t_idx,t in enumerate(T))
		min_dist = len(S)
		s_start =None
		s_end =None

		counter = len(pointers)
		start=None

		stack=None
		for i, s in enumerate(S):
			#print counter
			if s_end is not None and i-s_end>min_dist:
				pointers = dict((t_idx,-1) for t_idx,t in enumerate(T))
			if target.get(s):
				#print "current:",i,s			
				#print pointers
				if target[s]['cnt'] <2:
					t = target[s]['indices'][0]
					if pointers[t]==-1:
						counter-=1
						
					
					pointers[t] = i
				else:
					#print "occur",target[s]['occur']
					occur=target[s]['occur']
					t_idx=target[s]['indices'][occur]
					if pointers[t_idx]==-1:
						counter-=1
					pointers[t_idx]=i

					target[s]['occur'] = (occur+1) % target[s]['cnt']
				
				#if -1 not in pointers.values():
				if counter ==0 :
					
					start_idx,start = min(pointers.iteritems(), key=lambda x:x[1])
					#end_idx, end = max(pointers.iteritems(), key=lambda x:x[1])
					end = max(s_end,i)
					dist = end - start
					if dist < min_dist:
						min_dist = dist
						s_start = start
						s_end = end
					counter=1
					pointers[start_idx]=-1
					# print pointers
		
		if s_start is None:
			return ""
		#start, end=sorted(dist)[0][1]
		return S[s_start:s_end+1]



a=timeit.timeit()
sol = Solution()
# print sol.minWindow("aa","aa") 
# print sol.minWindow("aa","") 
# print sol.minWindow("bdab", "ab")
# print sol.minWindow("bbaa", "aba")
print sol.minWindow("bBbBBBBBBBBBBA", "BBA")
# print sol.minWindow("acbbaca", "aba")
# print sol.minWindow("ADOBECODEBANC","AB") 
print sol.minWindow("ADOBECODEBANC","ABC")
print sol.minWindow("eitwuyriguijgdijgijdpfjfdlsfhlsiduhflsiduhwewrohoshlfkudygykurdsfjfaafhouepirhqhahdluahflaiuhfliufhlisuhflaiuisglhauhskiufkdsgfslaoifslhiliushflfhlisgukygsuykglsyfglslshiua","fhfslul")
b= timeit.timeit()
print b-a
