# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # arr = []
        cnt = k
        res = -1
        def inorder(root):
            nonlocal cnt, res
            if root is None:
                return
            if cnt == 0:
                return
            inorder(root.left)
            # arr.append(root.val)
            cnt -= 1
            if cnt == 0:
                res = root.val
                return
            inorder(root.right)
        
        inorder(root)
        # return arr[k-1]
        return res