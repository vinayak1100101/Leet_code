class Solution:
    def countSeniors(self, details: List[str]) -> int:
        c=0
        for i in details:
            if(int(i[11:13])>60):
                
                c=c+1
        return c
        