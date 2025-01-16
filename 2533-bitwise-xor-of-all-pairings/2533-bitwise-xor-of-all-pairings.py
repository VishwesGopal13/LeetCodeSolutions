class Solution:
    def xorAllNums(self, nums1, nums2):
        n, m = len(nums1), len(nums2)
        counter = 0
        if n % 2 == 1:
            for num in nums2:
                counter ^= num
        if m % 2 == 1:
            for num in nums1:
                counter ^= num
        return counter