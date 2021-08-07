#https://leetcode.com/problems/count-of-smaller-numbers-after-self/


class BinaryIndexedTree:
    def __init__(self, max_size): #n = max_size
        self.size = max_size + 1
        self.tree = [0] * self.size
    def add_to_value_at(self, index, value): #add to value at index starting from 0 O(log n)
        i = index + 1 #in tree it's from 1
        while i < self.size: 
            self.tree[i] += value
            i += i & -i
    def get_sum(self, to_index, from_index = 0): 
        if from_index <= 0:
            i = to_index + 1 
            res = 0
            while i:
                res += self.tree[i]
                i -= i & - i
            return res
        else:
            return self.get_sum(to_index) - self.get_sum(from_index - 1)
    
    def get_value(self, index):
        return self.get_sum(to_index, to_index)
        
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        nsort = sorted(nums)
        nsort = [n for i, n in enumerate(nsort) if i == 0 or nsort[i - 1] != n]
        tree = BinaryIndexedTree(len(nsort))
        res = [0] * len(nums)
        for k, n in enumerate(reversed(nums)):
            i = bisect.bisect_left(nsort, n)
            tree.add_to_value_at(i, 1)
            res[len(nums) - k - 1] = tree.get_sum(i - 1) 
        return res
