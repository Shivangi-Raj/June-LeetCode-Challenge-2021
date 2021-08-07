#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def lca(root,p,q):
    if root==None:
        return None
    if root.val==p.val or root.val==q.val:
        return root
    a1=lca(root.left,p,q)
    a2=lca(root.right,p,q)
    if a1 and a2:
        return root
    if a1==None and a2==None:
        return None
    if a1==None:
        return a2
    return a1

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root==None:
            return None
        if root.val==p.val or root.val==q.val:
            return root
        ans=lca(root,p,q)
        return ans
