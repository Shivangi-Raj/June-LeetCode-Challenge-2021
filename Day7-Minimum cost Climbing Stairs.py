#https://leetcode.com/problems/min-cost-climbing-stairs/


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        ln=len(cost)
        if ln==2:
            return min(cost)
        d=[-1]*ln
        d[0]=cost[0]
        d[1]=cost[1]
        for i in range(2,ln):
            d[i]=min(d[i-1],d[i-2])+cost[i]
        ans=min(d[ln-1],d[ln-2])
        return ans
