class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans =[]
        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            left = k+1
            right = len(nums) -1
            while left<right:
                cur = nums[left] + nums[right]+nums[k]
                if cur < 0:
                    left+=1
                elif cur>0:
                    right-=1
                else: 
                    ans.append([nums[left],nums[right],nums[k]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left+=1
                    right -=1
        return ans