class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        has = set()
        ans = 0
        for r in range(len(s)):
            while s[r] in has:
                has.remove(s[left])
                left+=1
            has.add(s[r])
            ans = max(r - left +1, ans)
        return ans
