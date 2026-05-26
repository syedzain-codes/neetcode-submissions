class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        currMax = nums[0]
        currMin = nums[0]

        answer = nums[0]

        for i in range(1, len(nums)):

            num = nums[i]

            tempMax = max(num,num * currMax,num* currMin)

            tempMin = min(num,num * currMax,num * currMin)

            currMax = tempMax
            currMin = tempMin

            answer = max(answer, currMax)

        return answer 
                       
        