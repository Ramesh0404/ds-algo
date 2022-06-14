class Solution:
    def lengthOfLIS(self, nums):
        n=len(nums)
        l = [1]*n
        for i in range(1,n):
            for j in range(0,i):
                if nums[i]>nums[j] and l[i]<l[j]+1:
                    l[i]=l[j]+1
        maximum=0
        for i in range(n):  
            maximum=max(maximum, l[i])
        return maximum

a = [0,1,0,3,2,3]
r=Solution()
print(r.lengthOfLIS(a))