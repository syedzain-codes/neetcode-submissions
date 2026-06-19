class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left=1
        right=max(piles)
        while(left<right):
            sum=0
            mid=(left+right)//2
            for r in piles:
                sum+=(r+mid-1)//mid
            if sum<=h:
                
                right=mid
            else:
                left=mid+1
        return left




        