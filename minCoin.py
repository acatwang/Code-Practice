"""
Min coins
Given a list of coins type, target sum, return the possible combinations
Example:
minCoin([5,4,3],9) -> [5,4]
"""
import itertools



def minCoin(nums, target):
	table = {}
	for it in itertools.combinations(nums,2):
			s = sum(it)
			if s in table:
				table[s].append(it)
			else:
				table[s] = [(it)]

	if target in table:
		return table[target]
	else:
		return "No way"

print minCoin([5,4,3],9)
print minCoin([5,4,3,6],9)
print minCoin([5,4,3,6],20)

