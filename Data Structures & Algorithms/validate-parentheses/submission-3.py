class Solution:
    def isValid(self, s: str) -> bool:
        paran = {'(' : ')', '{' : '}', '[' : ']'}
        check = []
        for ch in s:
            if ch in paran.keys():
                check.append(ch)
            elif ch in paran.values():
                if check and ch == paran[check[-1]]:
                    check.pop()
                else:
                    return False
        if len(check) == 0:
            return True
        return False
        
            