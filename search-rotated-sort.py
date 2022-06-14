class Solution:
    def search(self, nums, target) -> int:
        if nums is None or len(nums)==0:
            return -1
        left=0
        right=len(nums)-1

        while left<right:
            mid=left+(right-left)//2
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid

        pivot=left
        left=0
        right= len(nums)-1

        if nums[pivot]<=target<=nums[right]:
            left = pivot
        else:
            right=pivot

        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return -1

nums = [4,5,6,7,0,1,2]
target = 0

# nums = [4,5,6,7,0,1,2]
# target = 3

# nums = [1]
# target = 0

s=Solution()
print(s.search(nums,target))

        