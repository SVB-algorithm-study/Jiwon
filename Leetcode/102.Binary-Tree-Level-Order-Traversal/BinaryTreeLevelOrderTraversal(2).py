# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = deque([root])

        while q:
            q_len = len(q)
            cur_level = []
            for i in range(q_len):
                node = q.popleft()
                if node:
                    cur_level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if cur_level:
                res.append(cur_level)

        return res
