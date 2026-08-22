class Solution:
    def inOrder(self, root):
        curr = root
        inorder = []

        while curr:
            if not curr.left:
                inorder.append(curr.data)
                curr = curr.right
            else:
                predecessor = curr.left
                while predecessor.right and predecessor.right != curr:
                    predecessor = predecessor.right

                if not predecessor.right:
                    predecessor.right = curr      # create thread
                    curr = curr.left
                else:
                    predecessor.right = None       # remove thread (restore tree)
                    inorder.append(curr.data)
                    curr = curr.right

        return inorder


"""
    Morris Inorder Traversal (Left -> Root -> Right)

    Time Complexity: O(n)
        - Each edge is traversed at most twice (once to create a thread,
          once to remove it). Total work is bounded by O(n), NOT O(n log n).

    Space Complexity: O(1) auxiliary
        - No stack, no recursion. Uses temporary "threads" (right pointers
          of predecessors) that are created and then removed, leaving the
          tree unchanged at the end. (Output list not counted as aux space.)

    Approach: For the current node:
      - No left child  -> visit it, move right.
      - Has left child -> find its inorder PREDECESSOR (rightmost node of
        the left subtree):
          * predecessor.right is None  -> thread it back to curr, go left.
          * predecessor.right == curr  -> left subtree done: remove thread,
            visit curr, go right.

    Tradeoff / Edge cases (Morris temporarily MUTATES the tree):
    Morris sets predecessor.right threads and removes them later. Because
    of this temporary mutation:
      1. Concurrency: during traversal the tree is in a modified state, so
         it is unsafe if another thread reads the tree concurrently.
      2. Interruption: if the traversal is interrupted partway (exception
         or early return), the tree is left CORRUPTED with dangling threads,
         since the code that removes each thread never runs.
    The stack-based iterative traversal avoids both issues (never mutates
    the tree) at the cost of O(h) auxiliary space.
"""


