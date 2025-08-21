class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        cur,res,fwd=0,0,0
        while fwd<len(nums):
            if nums[fwd]!=val:
                res+=1
                nums[cur]=nums[fwd]
                cur+=1
                fwd+=1
            else:
                fwd+=1
        return res