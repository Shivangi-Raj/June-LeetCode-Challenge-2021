class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        mod=10**9 + 7.
        verticalCuts.sort()
        horizontalCuts.sort()
        lnv=len(verticalCuts)
        lnh=len(horizontalCuts)
        maxv=verticalCuts[0]
        maxh=horizontalCuts[0]
             
        for i in range(1,lnv):
            cuts=verticalCuts[i]-verticalCuts[i-1]
            if cuts>maxv:
                maxv=cuts
        
        if (w-verticalCuts[-1])>maxv:
            maxv=w-verticalCuts[-1]
            
        for i in range(1,lnh):
            cuts=horizontalCuts[i]-horizontalCuts[i-1]
            if cuts>maxh:
                maxh=cuts
        
        if (h-horizontalCuts[-1])>maxh:
            maxh=h-horizontalCuts[-1]
        
        ans=((maxv%mod)*(maxh%mod))%mod
        
        return int(ans)
