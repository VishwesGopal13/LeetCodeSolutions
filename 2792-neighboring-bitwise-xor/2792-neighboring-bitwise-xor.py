class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        a = 0
        for i in derived:
            a = a ^ i
        if not(a):
            return True
        return False