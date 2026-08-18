class Solution:
    def isValid(self, s: str) -> bool:
        check = []
        has = {')': '(', '}': '{', ']': '['}

        for i in s:
            if i in has:
                if check and check[-1] == has[i]:
                    check.pop()
                else:
                    return False
            else:
                check.append(i)
            

        if check:
            return False
        else:
            return True