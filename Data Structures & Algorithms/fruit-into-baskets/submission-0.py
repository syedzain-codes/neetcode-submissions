class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dic={}
        l=0
        sum=0
        ans=0
        for r in range(0,len(fruits)):
            dic[fruits[r]]=dic.get(fruits[r],0)+1
            while len(dic)>2:
                dic[fruits[l]]-=1
                if dic[fruits[l]]==0:
                    del(dic[fruits[l]])
                l+=1
            ans=max(ans,r-l+1)
        return ans
        


                
        