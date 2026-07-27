class Solution:
    def constructBinaryTree(self, pre, preMirror):
        mirror_index = {val: i for i, val in enumerate(preMirror)}
        self.idx = 0
        n = len(pre)

        def build(lo, hi):
            if self.idx >= n or lo > hi:
                return None

            node = Node(pre[self.idx])
            self.idx += 1

            if lo == hi:
                return node

            # pre[self.idx] is the left child of current node.
            # In preMirror, children are swapped: right child comes first.
            # So in preMirror's sub-range [lo+1, hi]:
            #   [lo+1 ... split-1] = right subtree (in mirror order)
            #   [split ... hi]     = left subtree (in mirror order)
            # where split = mirror_index of the left child

            split = mirror_index[pre[self.idx]]

            node.left = build(split, hi)
            node.right = build(lo + 1, split - 1)

            return node

        return build(0, n - 1)
