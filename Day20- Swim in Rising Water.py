#https://leetcode.com/problems/swim-in-rising-water/

from heapq import heapify,heappush,heappop
# def valid(i,j,d,ln):
#     if i<0 or i>=ln or j<0 or j>=ln or (i,j) in d.keys():
#         return False
#     return True
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        h=[]
        heapify(h)
        d={}
        ln=len(grid)
        t=(grid[0][0],0,0)
        d[0,0]=1
        heappush(h,t)
        dirc=[(0,1),(1,0),(0,-1),(-1,0)]
        while(len(h)>0):
            a=heappop(h)
            ans=a[0]
            i=a[1]
            j=a[2]
            if i==ln-1 and j==ln-1:
                return ans
            for di in dirc:
                newr=i+di[0]
                newc=j+di[1]
                if (newr<0 or newc<0 or newr==ln or newc==ln or (newr,newc) in d.keys()):
                    continue
                else:
                    d[newr,newc]=1
                    val=max(ans,grid[newr][newc])
                    t=(val,newr,newc)        
                    heappush(h,t)
        
        return -1
