class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        has = {}
        left = 0
        if(len(s1)>len(s2)):
            return False
        s1count = Counter(s1)
        s2count = Counter(s2[:len(s1)])
        if s1count == s2count:
            return True
        for i in range(len(s1), len(s2)):
            s2count[s2[i]] += 1 
            s2count[s2[i-len(s1)]] -=1
            if s2count[s2[i-len(s1)]] == 0:
                del s2count[s2[i-len(s1)]]
            if s1count == s2count:
                return True
        return False


