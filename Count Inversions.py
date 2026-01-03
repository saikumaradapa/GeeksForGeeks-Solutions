class Solution:
    def inversionCount(self, arr):
        self.count = 0
        self.mergeSort(arr, 0, len(arr) - 1)
        return self.count

    def mergeSort(self, arr, l, r):
        if l >= r:
            return

        m = (l + r) // 2
        self.mergeSort(arr, l, m)
        self.mergeSort(arr, m + 1, r)
        self.merge(arr, l, m, r)

    def merge(self, arr, l, m, r):
        temp = []
        i, j = l, m + 1

        while i <= m and j <= r:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                self.count += (m - i + 1)
                j += 1

        temp.extend(arr[i:m+1])
        temp.extend(arr[j:r+1])

        arr[l:r+1] = temp


''' merge sort inversion logic
    time complexity : O(n logn)
    space complexity : O(n)
'''
