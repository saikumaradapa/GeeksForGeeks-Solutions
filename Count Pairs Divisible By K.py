class Solution:
    def countKdivPairs(self, arr, k):
        freq = [0] * k
        for num in arr:
            freq[num % k] += 1

        count = freq[0] * (freq[0] - 1) // 2  # pairs with remainder 0

        for i in range(1, k // 2 + 1):
            if i == k - i:
                count += freq[i] * (freq[i] - 1) // 2
            else:
                count += freq[i] * freq[k - i]

        return count
