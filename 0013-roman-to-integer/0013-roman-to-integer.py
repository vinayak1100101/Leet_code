class Solution:
    def romanToInt(self, s: str) -> int:
        dict={'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000}
        res=0
        i=0
        while(i<=len(s)-1):
            if(i==len(s)-1):
                    res=res+dict[s[-1]]
                    i=i+1
                    break
            if(dict[s[i]]>=dict[s[i+1]]):
                res=res+dict[s[i]]
                
                print(s[i])
                i=i+1
            else:
                
                res=res+dict[s[i+1]]-dict[s[i]]
                print(s[i],s[i+1])
                i=i+2
                
                
        return res


        