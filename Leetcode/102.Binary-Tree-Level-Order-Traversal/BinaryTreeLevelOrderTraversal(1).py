# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None:
            return
        q = deque([root])

        while q:
            cur_level = []
            for node in q:
                cur_level.append(node.val)
            res.append(cur_level)

            next_q = deque()
            while q:
                node = q.popleft()
                if node.left:
                    next_q.append(node.left)
                if node.right:
                    next_q.append(node.right)

            q = next_q

        return res
