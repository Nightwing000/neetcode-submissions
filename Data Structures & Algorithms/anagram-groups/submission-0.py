class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        an = dict()
        for i in strs:
            count = [0]*26
            for j in i:
                index = ord(j) - ord('a')
                count[index]+=1
            key = tuple(count)
            an[key] = an.get(key, []) + [i]
        return list(an.values())