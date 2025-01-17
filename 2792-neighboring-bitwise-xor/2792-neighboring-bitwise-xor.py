class Solution:
    def doesValidArrayExist(self, a: List[int]) -> bool:
        return sum(a)&1==0