class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return True if derived.count(1)%2 == 0 else False