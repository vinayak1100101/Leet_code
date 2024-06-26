class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        d=int(a,2)
        e=int(b,2)
        print(d+e)
        c=bin(d+e)
        c=c[2:]
        return c