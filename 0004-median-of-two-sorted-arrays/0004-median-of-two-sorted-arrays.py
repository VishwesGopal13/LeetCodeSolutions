class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B=nums1,nums2
        if len(B)<len(A):
            A,B=B,A
        n=len(A)+len(B)
        h=n//2

        l,r=0,len(A)-1
        while True:
            i=(l+r)//2
            j=h-i-2

            AL=A[i] if i>=0 else float('-inf')
            AR=A[i+1] if (i+1)<len(A) else float('inf')
            BL=B[j] if j>=0 else float('-inf')
            BR=B[j+1] if (j+1)<len(B) else float('inf')

            if AL<=BR and BL<=AR:
                if n%2==1:
                    return min(AR,BR)
                return (max(AL,BL)+min(AR,BR))/2
            elif AL>BR:
                r=i-1
            else:
                l=i+1