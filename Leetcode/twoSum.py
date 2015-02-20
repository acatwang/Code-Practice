"""
Given an array of integers, find two numbers such that they add up to a specific target number.
Return the non zero-based indices.

"""
import time
def twoSum_bruteforce(num,target):
    assert(len(num)>0)
    idx1=0
    idx2=0
    sorted_num = sorted(num) #[x for x in sorted(num) if x<=target]
    for a in sorted_num:
        for b in sorted_num:
            sum_ = a+b
            if sum_ ==target:
                # Note that a,b might be the same integer
                indices = sorted([i+1 for i,x in enumerate(num) if x==a or x==b])
                return (indices[0],indices[1])
            if sum_ >target:
                break
    return (None,None)

def twosum_hash(num,target):
    # O(n) runtime
    idx_table = dict(((val,idx+1) for idx,val in enumerate(num)))

    for i,n in enumerate(num):
        target_idx = idx_table.get(target-n)

        if target_idx:
            return (i+1,target_idx)


t0=time.time()
print twosum_hash([0,3,4,0],0)
t1 = time.time()
print t1-t0

t0=time.time()
print twoSum_bruteforce([0,3,4,0],0)
t1 = time.time()
print t1-t0

t0=time.time()
print twosum_hash([-3,5,3,90,4,6,800,6,4,13,5],0)  
t1 = time.time()
print t1-t0

t0=time.time()
print twoSum_bruteforce([-3,5,3,90,4,6,800,6,4,13,5],0)  
t1 = time.time()
print t1-t0