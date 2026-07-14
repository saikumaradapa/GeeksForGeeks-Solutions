class Solution:
    def find(self, arr):
        need = 0

        for a in reversed(arr):
            need = (need + a) // 2

        return need + 1
