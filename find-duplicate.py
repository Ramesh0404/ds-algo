class Solution:
    def findDuplicates(self, nums):
        dup_check=[]
        dup=[]
        for i in nums:
            if i in dup_check:
                dup.append(i)
            else:
                dup_check.append(i)
        return dup

a=[4,3,2,7,8,2,3,1]
r=Solution()
print(r.findDuplicates(a))