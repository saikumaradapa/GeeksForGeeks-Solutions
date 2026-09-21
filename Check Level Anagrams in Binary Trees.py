from collections import deque, Counter

class Solution:
    def areAnagrams(self, root1, root2):

        # BFS both trees level by level; compare each level's value multiset
        q1 = deque([root1] if root1 else [])
        q2 = deque([root2] if root2 else [])

        while q1 and q2:
            # both levels must have the same number of nodes
            if len(q1) != len(q2):
                return False

            level1 = []
            level2 = []

            # process current level of tree 1
            for _ in range(len(q1)):
                node = q1.popleft()
                level1.append(node.data)
                if node.left:
                    q1.append(node.left)
                if node.right:
                    q1.append(node.right)

            # process current level of tree 2
            for _ in range(len(q2)):
                node = q2.popleft()
                level2.append(node.data)
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)

            # anagram check: same values with same frequencies
            if Counter(level1) != Counter(level2):
                return False

        # both must finish at the same time (same number of levels)
        return not q1 and not q2
