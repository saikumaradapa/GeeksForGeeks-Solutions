class Solution:
    def isBalanced(self, root):
        _, is_balanced = self.get_height_and_balance(root)
        return is_balanced

    def get_height_and_balance(self, node):
        if not node:
            return 0, True

        left_height, left_balanced = self.get_height_and_balance(node.left)
        right_height, right_balanced = self.get_height_and_balance(node.right)

        height = 1 + max(left_height, right_height)
        is_balanced = (
            left_balanced
            and right_balanced
            and abs(left_height - right_height) <= 1
        )

        return height, is_balanced


''' time complexity : O(n)
    space complexity : O(h) auxiliary space
    returning tuples
'''

#######################################################################################################################################

class Solution:
    def isBalanced(self, root):
        return self.get_height(root) != -1

    def get_height(self, node):
        if not node:
            return 0

        left_height = self.get_height(node.left)
        if left_height == -1:
            return -1

        right_height = self.get_height(node.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return 1 + max(left_height, right_height)


''' time complexity : O(n)
    space complexity : O(h) auxiliary space
    this sentinel version shows you can tighten it up when asked "can you avoid returning two values?"
'''
