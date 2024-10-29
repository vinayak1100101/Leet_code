class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res=dict()
        for i in nums:
            if i in res.keys():
                res[i]=res[i]+1
            else:
                res[i]=1
        max=0
        k=0
        for i in res.keys():
            if res[i]>max:
                max=res[i]
                k=i
        return k
                