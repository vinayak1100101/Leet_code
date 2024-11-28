class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=s
        s2=t
        d1=dict()
        d2=dict()
        for i in s1:
            if i in d1.keys():
                d1[i]+=1
            else:
                d1[i]=1
        for i in s2:
            if i in d2.keys():
                d2[i]+=1
            else:
                d2[i]=1
        if d1==d2:
            return True
        else:
            return False
        