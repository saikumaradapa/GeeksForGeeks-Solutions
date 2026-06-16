class Solution:
    def constructList(self, queries):
        # track cumulative XOR from the end
        xor_all = 0
        arr = [0]  # initial value, will be XORed with final xor_all

        for q in queries:
            if q[0] == 0:
                # insert x, but it should NOT be affected by past XORs
                # it WILL be affected by future XORs
                # store x ^ xor_all so that when we apply xor_all at the end,
                # we get x ^ (future XORs only)
                arr.append(q[1] ^ xor_all)
            else:
                xor_all ^= q[1]

        # apply cumulative XOR to all elements
        res = [a ^ xor_all for a in arr]
        res.sort()
        return res
