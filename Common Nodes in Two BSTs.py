class Solution:
    def findCommon(self, r1: 'Node', r2: 'Node') -> list[int]:

        s1, s2 = [], []
        res = []
        a, b = r1, r2

        while True:
            # push the left spine of each tree onto its stack
            while a:
                s1.append(a)
                a = a.left
            while b:
                s2.append(b)
                b = b.left

            if not s1 or not s2:
                break                      # one tree is exhausted -> no more common values

            x, y = s1[-1], s2[-1]          # current smallest unvisited value in each tree
            if x.data == y.data:
                res.append(x.data)         # common value
                s1.pop(); s2.pop()
                a, b = x.right, y.right    # advance both
            elif x.data < y.data:
                s1.pop()
                a = x.right                # advance tree 1 only
            else:
                s2.pop()
                b = y.right                # advance tree 2 only

        return res

''' time complexity : O(n1 + n2)   (each node pushed and popped at most once)
    space complexity : O(h1 + h2)  (each stack holds one root-to-leaf path)
    approach to recall quickly

    - in-order traversal of a BST gives its values in sorted order
    - run two in-order traversals side by side, each with its own stack
      (iterative, so we can pause and resume them)
    - compare the current smallest unvisited value of each tree:
        equal   -> record it, advance both
        smaller -> advance that tree only
    - same idea as intersecting two sorted lists, without building the lists
    - results come out already sorted
    - verify: tree 1 in-order [0,1,4,5,7,9,10], tree 2 [4,7,9,10,20] -> [4,7,9,10]
'''
