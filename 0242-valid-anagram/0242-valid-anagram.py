class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        h=set(s)
        for i in h:
            if s.count(i) != t.count(i):
                return False
        return True