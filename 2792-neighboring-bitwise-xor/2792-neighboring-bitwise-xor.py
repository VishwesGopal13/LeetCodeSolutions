class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived) 
        def check_if_valid(original_0): 
            original = [0] * n 
            original[0] = original_0 
            for i in range(1, n): 
                original[i] = derived[i-1] ^ original[i-1] 
            return derived[-1] == (original[-1] ^ original[0]) 
        return check_if_valid(0) or check_if_valid(1)