class Solution:
    def first(self,nums,target):
        low_index=0
        high_index=len(nums)-1
        first=-1
        while low_index<=high_index:
            mid_index=low_index+(high_index-low_index)//2
            if target==nums[mid_index]:
                first=mid_index
                high_index=mid_index-1
            elif target<nums[mid_index]:
                high_index=mid_index-1
            else:
                low_index=mid_index+1
        return first
    
    def last(self,nums,target):
        low_index=0
        high_index=len(nums)-1
        last=-1
        while low_index<=high_index:
            mid_index=low_index+(high_index-low_index)//2
            if target==nums[mid_index]:
                last=mid_index
                low_index=mid_index+1
            elif target<nums[mid_index]:
                high_index=mid_index-1
            else:
                low_index=mid_index+1
        return last
    
    def searchRange(self,nums, target):
        return [self.first(nums, target), self.last(nums, target)]

nums=[5,7,7,8,8,10]
target=8

r=Solution()
s=r.searchRange(nums, target)
print(s)
