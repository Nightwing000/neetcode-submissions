class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
                l = str(len(i))
                i = l + "#" + i
                res += i 
        return res
    def decode(self, s: str) -> List[str]:
        fin = []
        i = 0 
        
        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            word = s[j + 1 : j + 1 + length]
            fin.append(word)

            i = j + 1 + length
        return fin

                