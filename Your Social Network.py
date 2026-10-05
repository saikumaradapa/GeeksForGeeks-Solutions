class Solution:
    def socialNetwork(self, arr):

        n = len(arr) + 1          # total users (arr has n-1 entries)

        # friend[i] = the single friend of user i (friend[i] < i); user 1 has none
        # arr[i-2] is the friend of user i, for i in 2..n
        friend = [0] * (n + 1)
        for i in range(2, n + 1):
            friend[i] = arr[i - 2]

        result = []
        # for each user i, follow the chain i -> friend[i] -> friend[...] collecting
        # (reachable user, #links). The chain is strictly decreasing, so it terminates.
        for i in range(2, n + 1):
            # record reachable user -> distance (links followed)
            dist = {}
            cur = i
            k = 0
            while friend[cur] != 0:
                cur = friend[cur]
                k += 1
                dist[cur] = k        # first time we reach 'cur' is the only time (tree chain)

            # output j from 1 to i-1 in increasing order, only reachable ones
            for j in range(1, i):
                if j in dist:
                    result.append([i, j, dist[j]])

        return result
