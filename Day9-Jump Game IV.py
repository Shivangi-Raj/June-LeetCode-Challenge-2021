#Day 1 - https://leetcode.com/problems/jump-game-vi/

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        ln=len(nums)
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return sum(nums)
        if k==1:
            ans=sum(nums)
            return ans
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        d = deque([(nums[0],0)])
        for i in range(1, len(nums)):
            dp[i] = nums[i] + d[0][0]
            
            while d and d[-1][0] < dp[i]:  
                d.pop()                    
            d.append((dp[i],i))             
            
            if i-k == d[0][1]:              
                d.popleft()                 
                
        return dp[-1]
        
