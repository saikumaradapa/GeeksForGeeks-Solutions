class Solution:
    def minimumCost(self, x, s, m, l, cs, cm, cl):

        INF = float('inf')

        # dp[a] = minimum cost to buy pizzas with total area AT LEAST a
        dp = [INF] * (x + 1)
        dp[0] = 0

        pizzas = [(s, cs), (m, cm), (l, cl)]

        for a in range(1, x + 1):
            for area, cost in pizzas:
                # buying this pizza covers 'area' units; remaining need is a-area,
                # but if that goes negative the requirement is already met -> clamp to 0
                prev = a - area
                if prev < 0:
                    prev = 0
                if dp[prev] + cost < dp[a]:
                    dp[a] = dp[prev] + cost

        return dp[x]
