class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        c=[]
        i=0
        j=0
        while(i<m and j<n):
            
            if(nums1[i]<nums2[j]):
                c.append(nums1[i])
                i=i+1
                    
            else:
                c.append(nums2[j])
                    
                j=j+1
        while(i<m):
            c.append(nums1[i])
            i=i+1
        while(j<n):
            c.append(nums2[j])
            j=j+1
        for i in range(len(nums1)):
            nums1[i]=c[i]
            
        