class Solution:
    def findMedian(self, root):
        """
        Returns the median value of the BST.
        For even n: returns V(n/2) (1-based index, so n//2-1 in 0-based)
        For odd n: returns V((n+1)/2) (1-based index, so n//2 in 0-based)
        Time complexity: O(n)
        Space complexity: O(h) for recursion stack
        """
        def findNodeCount(node):
            if not node:
                return 0
            return 1 + findNodeCount(node.left) + findNodeCount(node.right)
        
        def findKthNode(root, k, res):
            if root and res[0] == 0:
                findKthNode(root.left, k, res)
                k[0] -= 1 
                if k[0] == 0 and res[0] == 0:
                    res[0] = root.data
                    return
                findKthNode(root.right, k, res)
        
        node_count = findNodeCount(root)
        
        k = [node_count // 2] if node_count % 2 == 0 else [node_count // 2 + 1]
        res = [0]
        
        findKthNode(root, k, res)
        
        return res[0]


####################################################################################################################################################################################


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
