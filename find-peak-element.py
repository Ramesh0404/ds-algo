class Solution:
    def findPeakElement(self, nums):
        if len(nums) == 1:
            return 0
        if nums[len(nums)-1] > nums[len(nums)-2]:
            return len(nums)-1
        j=1
        k=len(nums)-2
        while j>k:
            check = (j+k)//2
            if nums[check]>nums[check+1] and nums[check]>nums[check-1]:
                return check
            elif nums[check] < nums[check+1]:
                j=check+1
            else:
                k=check+1
        return k

nums=[1,2,1,3,5,6,4]
r=Solution()
print(r.findPeakElement(nums))
