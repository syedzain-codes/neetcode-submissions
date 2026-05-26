class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1

        
        if nums[l] <= nums[r]:
            return nums[l]

        while l <= r:

            mid = (l + r) // 2

            
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]

            
            if nums[mid] > nums[r]:
                l = mid + 1

            
            else:
                r = mid - 1    

            
              