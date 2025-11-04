class Solution:
    # returns the inorder successor of the Node x in BST (rooted at 'root')
    def inorderSuccessor(self, root, x):
        curr = root
        successor = -1
        while curr:
            if curr.data > x.data:
                successor = curr.data
                curr = curr.left
            else:
                curr = curr.right
        return successor
        
''' 
    time complexity : O(logn)
    space complexity : O(1)
'''
