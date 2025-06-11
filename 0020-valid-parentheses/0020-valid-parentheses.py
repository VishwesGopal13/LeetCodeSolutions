class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        brckt={')':'(',']':'[','}':'{'}
        for char in s:
            if char in brckt:
                if not stk or stk[-1]!=brckt[char]:
                    return False
                stk.pop()
            else:
                stk.append(char)
        return not stk