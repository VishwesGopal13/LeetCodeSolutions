class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B=nums1,nums2
        n=len(A)+len(B)
        h=n//2
        if len(B)<len(A):
            A,B=B,A
        l,r=0,len(A)-1
        while True:
            i=(l+r)//2
            j=h-i-2
            Al=A[i] if i>=0 else float('-inf')
            Ar=A[i+1] if i+1<len(A) else float('inf')
            Bl=B[j] if j>=0 else float('-inf')
            Br=B[j+1] if j+1<len(B) else float('inf')

            if Al<=Br and Bl<=Ar:
                if n%2==1:
                    return min(Ar,Br)
                return (max(Al,Bl)+min(Ar,Br))/2
            elif Al>Br:
                r=i-1
            else:
                l=i+1