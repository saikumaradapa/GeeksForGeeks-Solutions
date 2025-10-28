class Solution:
    def tree_traversal(self, root):
        if not root: return [[],[],[]]
        preorder = []
        inorder = []
        postorder = []
        stack = [(root, 1)]

        while stack:
            curr, count = stack.pop()
            if not curr: 
                continue
            if count == 1:
                preorder.append(curr.val)
                stack.append((curr, count+1))
                stack.append((curr.left, 1))
            elif count == 2:
                inorder.append(curr.val)
                stack.append((curr, count+1))
                stack.append((curr.right, 1))
            else:
                postorder.append(curr.val)

        return [preorder, inorder, postorder]

''' 
  time complexity : O(3 N)
  space complexity : O(3 N)
'''
