class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        og = dict()
        comp = dict()
        for i in s:
            if i not in og:
                og[i] = 0
            og[i] += 1
        for i in t:
            if i not in comp:
                comp[i] = 0
            comp[i] += 1
        if og == comp:
            return True
        else:
            return False