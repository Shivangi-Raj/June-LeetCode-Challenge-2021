#https://leetcode.com/problems/maximum-performance-of-a-team/


import heapq
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:

        d=[]
        mod=1000000007
        
        for i in range(n):
            t=(efficiency[i],speed[i])
            d.append(t)
        
        d.sort(reverse=True)
        s=0
        ans=0
        q=[]
        heapq.heapify(q)
        
        for i in range(n):
            eff=d[i][0]
            s+=d[i][1]
            ans=max(ans,s*eff)
            heapq.heappush(q,d[i][1])
            if len(q)>k-1:
                a=heapq.heappop(q)
                s-=a
        
        return int(ans%mod)
