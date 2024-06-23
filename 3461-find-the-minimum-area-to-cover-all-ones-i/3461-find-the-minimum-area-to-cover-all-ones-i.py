import numpy
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        p1=len(grid[0])
        p2=0
        p11=len(grid)
        p22=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if(grid[i][j]==1):
                    p1=min(p1,j)
                    p11=min(p11,i)
                    p2=max(p2,j)
                    p22=max(p22,i)

        print(p1,p2,p11,p22)
        return (p2-p1+1)*(p22-p11+1)
        
            
        
        