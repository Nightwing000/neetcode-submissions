class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref =[]
        curr = 1
        suf = []
        for i in nums:
            pref.append(curr)
            curr *= i
        curr = 1
        for i in reversed(nums):
            suf.append(curr)
            curr *= i
        res = []
        # Match pref[i] with suf from the other end
        for i in range(len(nums)):
            res.append(pref[i] * suf[len(nums) - 1 - i])
        return res