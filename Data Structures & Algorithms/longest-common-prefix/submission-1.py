class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = ""
        for i in range(0, len(strs[0])):
            for j in range(1,len(strs)):
                if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                    return pref
            pref += strs[0][i]
        return pref