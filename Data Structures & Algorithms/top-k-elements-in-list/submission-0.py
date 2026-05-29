class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()

        x = []
        l = 0
        r = 1
        fc = 1

        while r < len(nums):
            if nums[l] == nums[r]:
                fc += 1
                r += 1
            else:
                x.append((nums[l], fc))
                fc = 1
                l = r
                r = l + 1

        x.append((nums[l], fc))

        x.sort(key=lambda t: t[1], reverse=True)

        ans = []

        for i in range(k):
            ans.append(x[i][0])

        return ans
                
             
                
               


        
        
        
        