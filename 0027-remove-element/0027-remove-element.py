class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c=0
        res=list()
        nums1=[]
        
        print(nums)
        for i in nums:
            if i==val:
                c=c+1
            else:
                res.append(i)
        for i in range(c):
            res.append('_')
        for i in range(len(nums)):
            nums[i]=res[i]
        print(nums)
        return len(nums)-c
        
        