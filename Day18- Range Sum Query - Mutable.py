#https://leetcode.com/problems/range-sum-query-mutable/
#Soln- Use the concept Segment Tree

class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.a, self.c = nums, [0] * (self.n + 1)
        for i in range(self.n):
            k = i + 1
            while k <= self.n:
                self.c[k] += nums[i]
                k += (k & -k)

        # print(self.s)            
    def update(self, i: int, val: int) -> None:
        
        diff, self.a[i] = val - self.a[i], val
        i += 1
        while i <= self.n:
            self.c[i] += diff
            i += (i & -i)
        

    def sumRange(self, i: int, j: int) -> int:
        # if left==right:
        #     return self.nums[left]
        res, j = 0, j + 1
        while j:
            res += self.c[j]
            j -= (j & -j)
        while i:
            res -= self.c[i]
            i -= (i & -i)
        return res

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
