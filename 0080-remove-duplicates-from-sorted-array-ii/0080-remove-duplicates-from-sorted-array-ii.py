class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current=nums[0]
        count=1
        c=0
        res=[]
        for i in range(len(nums)):
            if (current !=nums[i]):
                c=0
            if(current !=nums[i] or c<2):
                current=nums[i]
                res.append(nums[i])
                count=count+1
                c=c+1
            
        for i in range(len(nums)):
            if(i<len(res)):
                nums[i]=res[i]
            else:
                nums[i]='_'
        return len(res)
                

        