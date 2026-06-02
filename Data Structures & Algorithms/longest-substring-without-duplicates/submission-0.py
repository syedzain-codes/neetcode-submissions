class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        a = set()
        maximum = 0

        for r in range(len(s)):

            while s[r] in a:
                a.remove(s[l])
                l += 1

            a.add(s[r])

            maximum = max(maximum, r - l + 1)

        return maximum   
               
            
        
        
        
        
