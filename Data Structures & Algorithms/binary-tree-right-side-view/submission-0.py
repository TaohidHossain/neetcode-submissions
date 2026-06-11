# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        q = [root]
        res = []
        while q:
            sz = len(q)
            # level = []
            rightMost = None
            for _ in range(sz):
                curr = q.pop(0)
                # level.append(curr.val)
                rightMost = curr
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            # res.append(level[-1])
            res.append(rightMost.val)

        return res

