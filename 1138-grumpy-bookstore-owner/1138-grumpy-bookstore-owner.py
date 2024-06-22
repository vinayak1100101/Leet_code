class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        res=0
        r=list()
        for i in range(len(grumpy)):
            if(grumpy[i]==0):
                res=res+customers[i]
        for i in range(len(grumpy)-minutes+1):
            s=0
            for j in range(i,i+minutes):
                if(grumpy[j]!=0):
                    s=s+customers[j]
            r.append(int(s))
        res=res+max(r)
        return res
            
        