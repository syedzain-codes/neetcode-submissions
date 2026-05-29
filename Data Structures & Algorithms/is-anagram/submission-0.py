class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x=[0]*26
        y=[0]*26
        for i in s:

            x[ord(i)-ord("a")]+=1
        for i in t:
            y[ord(i)-ord("a")]+=1
        if x==y:
            return True
        else:
            return False     



        