#https://leetcode.com/problems/open-the-lock/

from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:    
        start="0000"
        if start in deadends:
            return -1
        if start==target:
            return 0
        dead_set = set(deadends)
        queue = collections.deque([('0000', 0)])
        visited = set('0000')

        while queue:
            (string, steps) = queue.popleft()
            if string == target:
                return steps
            elif string in dead_set:
                continue
            for i in range(4):
                digit = int(string[i])
                for move in [-1, 1]:
                    new_digit = (digit + move) % 10
                    new_string = string[:i]+str(new_digit)+string[i+1:]
                    if new_string not in visited:
                        visited.add(new_string)
                        queue.append((new_string, steps+1))
        return -1