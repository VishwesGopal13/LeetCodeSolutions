class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        fin=[]
        for i in range(0,len(s),k):
            fin.append(s[i:i+k])
        if len(fin[-1])<k:
            fin[-1]=fin[-1].ljust(k,fill)
        return fin