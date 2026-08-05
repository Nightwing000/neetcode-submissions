class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        has = {}
        for num in nums:
            if num not in has:
                has[num] = 1
            has[num]+=1

        return max(has, key=has.get)
            