from typing import List, Optional

'''
  Solving using recursion. It is more elegant.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        self.inorder(root, ret)
        return ret

    def inorder(self, node: Optional[TreeNode], ret: List[int]):
        if node is None:
            return

        self.inorder(node.left, ret)
        ret.append(node.val)
        self.inorder(node.right, ret)
        return
