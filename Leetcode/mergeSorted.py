class Test(object):
    def validate(self):
        print self.nums1
    def merge(self,nums1, m, nums2, n):
        midx=0
        while(len(nums2)>0):
            print nums2
            ncurr = nums2[0]
            for i in range(midx,m):

                if ncurr > nums1[i]:
                    nums1.insert(midx,ncurr)
                    nums2.pop(0)
                    break
                else:
                    if i==m:
                        nums1.append(ncurr)
                        nums2.pop(0)
            print len(nums2)
        self.nums1=nums1

t = Test()
t.merge([],0,[3],1)
t.validate()
