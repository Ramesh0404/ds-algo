class Solution:
    def first(self,nums,target):
        left=0
        right=len(nums)-1
        first=-1
        while left<=right:
            middle=left+(right-left)//2
            if target==nums[middle]:
                first=middle
                right=middle-1
            elif target<nums[middle]:
                right=middle-1
            else:
                left=middle+1
        return first
    
    def last(self,nums,target):
        left=0
        right=len(nums)-1
        last=-1
        while left<=right:
            middle=left+(right-left)//2
            if target==nums[middle]:
                last=middle
                left=middle+1
            elif target<nums[middle]:
                right=middle-1
            else:
                left=middle+1
        return last
    
    def searchRange(self,nums, target):
        return [self.first(nums, target), self.last(nums, target)]
        
