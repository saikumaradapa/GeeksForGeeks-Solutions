class Solution:
    def getSize(self, root):
        if not root:
            return 0
        return 1 + self.getSize(root.left) + self.getSize(root.right)

'''
    count current node + left subtree size + right subtree size
    time complexity : O(n)
    space complexity : O(h) where h = height of tree (recursion stack)
'''
