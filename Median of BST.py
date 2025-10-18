class Solution:
    def findMedian(self, root):
        # Step 1: Count the total number of nodes using Morris Traversal
        def count_nodes(node):
            count = 0
            current = node
            while current:
                if not current.left:
                    count += 1
                    current = current.right
                else:
                    pre = current.left
                    while pre.right and pre.right != current:
                        pre = pre.right
                    if not pre.right:
                        pre.right = current
                        current = current.left
                    else:
                        pre.right = None
                        count += 1
                        current = current.right
            return count

        # Step 2: Find the median using Morris Traversal
        def find_kth(node, k):
            cnt = 0
            current = node
            while current:
                if not current.left:
                    cnt += 1
                    if cnt == k:
                        return current.data
                    current = current.right
                else:
                    pre = current.left
                    while pre.right and pre.right != current:
                        pre = pre.right
                    if not pre.right:
                        pre.right = current
                        current = current.left
                    else:
                        pre.right = None
                        cnt += 1
                        if cnt == k:
                            return current.data
                        current = current.right
            return None

        n = count_nodes(root)
        # If number of nodes is even: return V(n//2)
        # If number of nodes is odd: return V((n+1)//2)
        if n % 2 == 0:
            median = find_kth(root, n // 2)
        else:
            median = find_kth(root, (n + 1) // 2)
        return median
