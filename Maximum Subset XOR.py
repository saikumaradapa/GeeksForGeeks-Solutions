class Solution:
    def maxSubsetXOR(self, arr):
        # Gaussian elimination on the XOR basis
        n = len(arr)
        # Find highest bit position
        max_bit = 20  # since arr[i] <= 10^6 < 2^20

        index = 0
        for bit in range(max_bit, -1, -1):
            # Find element with this bit set, starting from index
            pivot = -1
            for j in range(index, n):
                if arr[j] & (1 << bit):
                    pivot = j
                    break

            if pivot == -1:
                continue

            # Swap pivot to current index
            arr[index], arr[pivot] = arr[pivot], arr[index]

            # Eliminate this bit from all other elements
            for j in range(n):
                if j != index and arr[j] & (1 << bit):
                    arr[j] ^= arr[index]

            index += 1

        # XOR all basis elements for maximum
        result = 0
        for i in range(index):
            result ^= arr[i]

        return result
