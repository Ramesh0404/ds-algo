class Solution:
    def findDuplicates(self, nums):
        new = []
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        for k,v in count.items():
            if v > 1:
                new.append(k)
            else:
                pass
        return new

a=[4,3,2,7,8,2,3,1]
r=Solution()
print(r.findDuplicates(a))