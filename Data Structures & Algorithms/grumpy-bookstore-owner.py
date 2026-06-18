class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        sum=0
        
        for i in range(0,len(grumpy)):
            if grumpy[i]==0:
                sum+=customers[i]
        saved=0
        maxsaved=0
        left=0

       
        for right in range(0,len(grumpy)):
            if grumpy[right]==1:
                saved+=customers[right]
            if right-left+1>minutes:
                if grumpy[left]==1:


                    saved-=customers[left]
                left+=1
            if right-left+1==minutes:
                maxsaved=max(saved,maxsaved)
        return sum+maxsaved




            
        
