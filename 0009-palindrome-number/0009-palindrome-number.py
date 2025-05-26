class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        rs = s[::-1]
        if s==rs:
            return True
        else:
            return False