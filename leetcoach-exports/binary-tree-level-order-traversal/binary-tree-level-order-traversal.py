# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        res = []
        q = deque()
        q.append(root)
        while q:
            cnt = len(q)
            i = 0
            appendArray = []
            while i < cnt:
                curr = q.popleft()
                appendArray.append(curr.val)
                if curr.left is not None:
                    q.append(curr.left)
                if curr.right is not None:
                    q.append(curr.right)
                i += 1
            res.append(appendArray)
        return res
            
#   0
#  2 4
# 1  
