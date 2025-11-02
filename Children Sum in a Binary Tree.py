class Solution:
    def isSumProperty(self, root):
        if not root or (not root.left and not root.right):
            return True
        left_val = root.left.data if root.left else 0
        right_val = root.right.data if root.right else 0
        return self.isSumProperty(root.left) and self.isSumProperty(root.right) and (root.data == left_val + right_val)
        
''' 
    time complexity : O(n)
    space complexity : O(h)
'''
