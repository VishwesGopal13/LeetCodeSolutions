class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_palindrome(s):
            return s==s[::-1]
        def n_to_base_k(num,k):
            if num==0:
                return "0"
            digit=[]
            while num>0:
                digit.append(str(num%k))
                num=num//k
            return "".join(digit[::-1])
        count=0
        sum=0
        length=1
        while count<n:
            for i in range(10**(length-1),10**length):
                s=str(i)
                nstr=s+s[:-1][::-1]
                num=int(nstr)
                base_k=n_to_base_k(num,k)
                if is_palindrome(base_k):
                    count=count+1
                    sum=sum+num
                    if count==n:
                        return sum
            for i in range(10**(length-1),10**length):
                s=str(i)
                nstr=s+s[::-1]
                num=int(nstr)
                base_k=n_to_base_k(num,k)
                if is_palindrome(base_k):
                    count=count+1
                    sum=sum+num
                    if count==n:
                        return sum
            length=length+1
        return sum