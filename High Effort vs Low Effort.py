class Solution:
    def maxTask(self, h: list[int], l: list[int]) -> int:
        n = len(h)
        # rest = max tasks if previous day we did nothing (or it's day 0)
        # work = max tasks if previous day we did some task (low or high)
        rest = 0  # no tasks done yet, "rested" before day 0
        work = 0  # not possible before day 0, but 0 works as base

        for i in range(n):
            new_rest = max(rest, work)          # skip today
            new_work = max(
                rest + h[i],                    # high-effort (only if prev was rest)
                max(rest, work) + l[i]          # low-effort (can follow anything)
            )
            rest, work = new_rest, new_work

        return max(rest, work)
