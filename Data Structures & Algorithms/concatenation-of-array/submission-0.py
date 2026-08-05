class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        j = 0
        #while j<=1:
        for i in nums:
            ans.append(i)
            #j+=1
        
        return ans*2