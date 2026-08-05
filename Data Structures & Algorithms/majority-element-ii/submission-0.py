from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        main = len(nums)/3
        has = Counter(nums)
        ans = [k for k, v in has.items() if v > main]
        return ans
