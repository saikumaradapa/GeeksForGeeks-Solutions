class Solution:
    def isSubTree(self, root1, root2):
        if not root2:
            return True
        if not root1:
            return False
        if self.check(root1, root2):
            return True
        return self.isSubTree(root1.left, root2) or self.isSubTree(root1.right, root2)

    def check(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        if node1.data != node2.data:
            return False
        return self.check(node1.left, node2.left) and self.check(node1.right, node2.right)

'''
    for each node in T, check if subtree matches S
    check() compares two trees for identical structure and values
    time complexity : O(n * m)
    space complexity : O(h) where h = height of T (recursion stack)
'''
