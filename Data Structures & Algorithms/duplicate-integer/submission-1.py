class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:

        dup = {}

        for i, n in enumerate(nums):

            if n in dup:
                return True

            else:
                dup[n] = 1

        return False    

        
     
            
        