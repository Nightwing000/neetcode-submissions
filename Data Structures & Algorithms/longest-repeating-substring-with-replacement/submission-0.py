class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        has = dict()
        left = 0
        ans = 0
        maxf = 0
        for right in range(len(s)):
            has[s[right]] = has.get(s[right],0)+1
            maxf = max(maxf, has[s[right]])
            while right-left+1 - maxf> k:
                has[s[left]] -=1
                left +=1
            ans = max(ans, right-left+1)

        return ans