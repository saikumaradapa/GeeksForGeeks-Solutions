class Solution:
    def toSumTree(self, root):
        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            temp = root.data
            root.data = left + right
            return temp + left + right
        helper(root)
        return root

'''
    helper returns total sum of subtree (original values)
    each node's new value = sum of left + right subtree (original values)
    return original value + left + right so parent can use it
    time complexity : O(n)
    space complexity : O(height)
'''
