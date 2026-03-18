class Solution:
    def distCandy(self, root):
        res = [0]
        self.dfs(root, res)
        return res[0]
    def dfs(self, curr, res):
        if not curr: return [0, 0]

        l_size, l_coins = self.dfs(curr.left, res)
        r_size, r_coins = self.dfs(curr.right, res)

        size = 1 + l_size + r_size
        coins = curr.data + l_coins + r_coins
        res[0] += abs(size-coins)

        return [size, coins]
