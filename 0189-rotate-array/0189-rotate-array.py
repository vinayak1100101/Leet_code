class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        res=[]
        k=k%len(nums)
        nums.reverse()
        nums[:k]=reversed(nums[:k])
        nums[k:]=reversed(nums[k:])