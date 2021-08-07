#https://leetcode.com/problems/out-of-boundary-paths/

def count(dp,sr,sc,mm,m,n):
    # print(sr,sc,mm,dp)
    if mm<0:
        return 0
    if sr<0 or sr==m or sc<0 or sc==n:
        return 1
    if (sr,sc,mm) in dp.keys():
        return dp[sr,sc,mm]
    d=[(0,1),(0,-1),(-1,0),(1,0)]
    c=0
    for it in d:
        x=sr+it[0]
        y=sc+it[1]
        # print("going",x,y)
        c+=count(dp,x,y,mm-1,m,n)
    
    c=c%1000000007
    dp[sr,sc,mm]=c
    return c

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if maxMove==0:
            return 0
        if m==1 and n==1:
            return 4
        
        dp={}
        cn=0       
        cn=count(dp,startRow,startColumn,maxMove,m,n)      
        return cn%1000000007
        
