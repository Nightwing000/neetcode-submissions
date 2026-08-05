class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = len(nums)-2
        right = len(nums) -1 
        k = 0
        while left>=0 and right>0:
            if nums[left] ==  nums[right]:
                del nums[right]
            left-=1
            right-=1
        return len(nums)