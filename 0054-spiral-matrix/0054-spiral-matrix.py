class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans=[]
        m,n=len(matrix),len(matrix[0])
        i,j=0,0
        U,R,D,L=0,1,2,3
        direction=R

        RWALL=n
        DWALL=m
        LWALL=-1
        UWALL=0
        
        while len(ans)!=m*n:
            if direction==R:
                while j<RWALL:
                    ans.append(matrix[i][j])
                    j+=1
                i,j=i+1,j-1
                RWALL-=1
                direction=D
            elif direction==D:
                while i<DWALL:
                    ans.append(matrix[i][j])
                    i+=1
                i,j=i-1,j-1
                DWALL-=1
                direction=L
            elif direction==L:
                while j>LWALL:
                    ans.append(matrix[i][j])
                    j-=1
                i,j=i-1,j+1
                LWALL+=1
                direction=U
            elif direction==U:
                while i>UWALL:
                    ans.append(matrix[i][j])
                    i-=1
                i,j=i+1,j+1
                UWALL+=1
                direction=R
        return ans