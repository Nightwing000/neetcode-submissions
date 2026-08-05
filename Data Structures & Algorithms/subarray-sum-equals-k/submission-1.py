class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0:1} #accounting for first index ?idk i forgot
        curr_sum = 0
        ans = 0

        for i in nums:
            curr_sum+= i
            target = curr_sum - k

            if target in seen:
                ans += seen[target]
            seen[curr_sum] = seen.get(curr_sum, 0) + 1

        return ans