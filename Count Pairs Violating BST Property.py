class Solution:
    def pairsViolatingBST(self, root):

        # Step 1: iterative in-order traversal (avoids recursion limits on deep trees)
        vals = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            vals.append(cur.data)
            cur = cur.right

        # Step 2: count inversions with bottom-up merge sort
        n = len(vals)
        arr = vals
        tmp = [0] * n
        inv = 0
        width = 1
        while width < n:
            for lo in range(0, n, 2 * width):
                mid = min(lo + width, n)
                hi = min(lo + 2 * width, n)
                i, j, k = lo, mid, lo
                while i < mid and j < hi:
                    if arr[i] <= arr[j]:
                        tmp[k] = arr[i]; i += 1
                    else:
                        tmp[k] = arr[j]; j += 1
                        inv += mid - i      # every remaining left element > arr[j]
                    k += 1
                while i < mid:
                    tmp[k] = arr[i]; i += 1; k += 1
                while j < hi:
                    tmp[k] = arr[j]; j += 1; k += 1
            arr, tmp = tmp, arr
            width *= 2

        return inv
