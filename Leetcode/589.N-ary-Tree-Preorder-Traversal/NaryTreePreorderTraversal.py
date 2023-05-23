"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: "Node") -> List[int]:
        traversal = []
        # print(root.children)

        def preorderTraversalHelper(root):
            if root:
                traversal.append(root.val)
                children = deque(root.children)
                while children:
                    child = children.popleft()
                    preorderTraversalHelper(child)

        preorderTraversalHelper(root)

        return traversal
