class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        res=[]
        k=k%len(nums)
        for i in range(len(nums)-k,len(nums)):
            res.append(nums[i])
        for i in range(len(nums)-k):
            res.append(nums[i])
        for i in range(len(nums)):
            nums[i]=res[i]
        return res
        