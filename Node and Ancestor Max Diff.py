class Solution:
    def maxDiff(self, root):

        self.ans = float('-inf')

        def dfs(node, max_ancestor):
            if node is None:
                return
            # if this node has an ancestor, try forming a pair
            if max_ancestor is not None:
                self.ans = max(self.ans, max_ancestor - node.data)
            # pass down the largest ancestor value seen on this path
            new_max = node.data if max_ancestor is None else max(max_ancestor, node.data)
            dfs(node.left, new_max)
            dfs(node.right, new_max)

        dfs(root, None)
        return self.ans

''' time complexity : O(n)
    space complexity : O(n)   (recursion stack, worst case skewed tree)
    approach to recall quickly

    - want to maximize A - B where A is an ancestor of B
    - for any descendant B, the best A is the LARGEST ancestor value on its path
    - DFS downward carrying max_ancestor = max node value seen among ancestors
    - at each node (that has an ancestor): candidate = max_ancestor - node.data
    - recurse with updated max_ancestor = max(max_ancestor, node.data)
    - root passes None (no ancestor) so it never forms a pair as descendant
    - answer can be negative (e.g. strictly increasing path) -> init to -inf
'''
