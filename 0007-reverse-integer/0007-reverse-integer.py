class Solution:
    def reverse(self, x: int) -> int:
        c=1
        if(x<0):
            c=-1
            x=x*-1
        x=str(x)
        x=x[::-1]
        x=int(x)
        if(x*c>2147483647 or x*c<-2147483648):
            return 0
        return x*c
        
        