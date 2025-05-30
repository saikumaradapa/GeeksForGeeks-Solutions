class Solution:
    def findMaxFork(self, root, k):
        result = -1  # or use None if you want to handle "not found" case
        while root:
            if root.data <= k:
                result = root.data
                root = root.right
            else:
                root = root.left
        return result
