class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numhas = set(nums)
        ans = 0
        for i in numhas:
            if i-1 not in numhas:
                cur = i+1
                temp = 1
                while cur in numhas:
                    cur+=1
                    temp+=1
                ans = max(ans,temp)
                
                    
        return ans