class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        ans = ""
        i =0
        
        if l1 == l2:
            while i< l1:
                ans+= word1[i] + word2[i]
                i+= 1
            return ans
        elif l1> l2:
            while i< l2:
                ans+= word1[i] + word2[i]
                i+= 1
            return ans + word1[i:]
        else:
            while i< l1:
                ans+= word1[i] + word2[i]
                i+= 1
            return ans + word2[i:]
