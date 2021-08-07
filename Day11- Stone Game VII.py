#https://leetcode.com/problems/stone-game-vii/

def solve(stone,i,j,d,s):
    if i>j:
        return 0
    # print(i,j,stone,stone[i],stone[j])
    if (i,j) in d.keys():
        return d[i,j]
    a1=(s-stone[i])-solve(stone,i+1,j,d,s-stone[i])
    a2=(s-stone[j])-solve(stone,i,j-1,d,s-stone[j])
    d[i,j]=max(a1,a2)
    # print(a1,a2)
    return d[i,j]
    

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        
        ln=len(stones)
        if ln==2:
            return abs(stones[0]-stones[1])
        
        d={}
        s=sum(stones)
        ans=solve(stones,0,ln-1,d,s)
        return ans
