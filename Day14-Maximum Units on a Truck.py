#https://leetcode.com/submissions/detail/507777483/

import heapq
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        for i in boxTypes:
            i[0],i[1]=-i[1],i[0]
        # print(boxTypes)
        ans=0
        heapq.heapify(boxTypes)
        while(len(boxTypes)>0):
            a=heapq.heappop(boxTypes)
            # print(truckSize,ans,a)
            if a[1]<truckSize:
                ans+=(a[1]*-a[0])
                truckSize-=a[1]
            else:
                ans+=(truckSize*-a[0])
                truckSize=0
            if truckSize<=0:
                break
        
        return ans
                
