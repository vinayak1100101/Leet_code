class Solution:
    def countDigits(self, num: int) -> int:
        c=0
        a=num
        while(num!=0):
            if(a%(num%10)==0):
                c=c+1
            num=int(num/10)
        return c
        