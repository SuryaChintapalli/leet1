# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        def postorder(ptr):
            if ptr:
                result.append(ptr.val)
                postorder(ptr.left)
                postorder(ptr.right)
                
        postorder(root)
        return result
        
        
