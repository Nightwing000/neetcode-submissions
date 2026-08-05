class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = dict()
        for i in strs:
            count = [0]*26
            for j in i:
                ind = ord(j) - ord('a')
                count[ind] += 1
            key = tuple(count)
            if key not in ans:
                ans[key] = []
            ans[key].append(i)
        return list(ans.values())