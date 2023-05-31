#BFS SOLUTION

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        res = 0


        if not root:
            return 0


        q = collections.deque([root])


        while q:

            node = q.popleft()

            if low <= node.val <= high:
                res += node.val

            if node.left and node.val > low:
                q.append(node.left)

            if node.right and node.val < high:
                q.append(node.right)



        return res
      
      
     
    
#DFS SOLUTION

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        if not root:
            return 0


        root_val = root.val if low <= root.val <= high else 0
        left_val = self.rangeSumBST(root.left, low, high) if root.val > low else 0
        right_val = self.rangeSumBST(root.right, low, high) if root.val < high else 0

        return root_val + left_val + right_val

