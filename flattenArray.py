"""
Flatten an array containing subarrays and strings. 
Return an one-dim array 
"""
def flatten(arr):
	flattened = []
	[ map(flattened.append,x) if type(x)==list else flattened.append(x) for x in arr]
	return flattened


arr = [[1,2,3],[4,5,6], [7], [8,9],'hi','there']
print flatten(arr)