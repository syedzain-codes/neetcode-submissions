class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1={}
        for s in s1:
            dic1[s]=dic1.get(s,0)+1
        left=0
        dic2={}
        
        for right in range(len(s2)):
            
            dic2[s2[right]] = dic2.get(s2[right], 0) + 1
            
           
            if right - left + 1 > len(s1):
                dic2[s2[left]] -= 1
                if dic2[s2[left]] == 0:
                    del dic2[s2[left]]
                left += 1
            
            
            if dic1 == dic2:
                return True
        
        return False
                

        