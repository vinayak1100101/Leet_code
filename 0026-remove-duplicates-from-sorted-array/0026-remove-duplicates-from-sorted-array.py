class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res=[]
        for i in nums:
            if i in res:
                continue
            else:
                res.append(i)
        for i in range(len(nums)):
            if i<len(res):
                nums[i]=res[i]
            else:
                nums[i]='_'
        return len(res)
        