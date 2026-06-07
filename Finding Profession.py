class Solution:
    def profession(self, level, pos):
        flips = 0
        while pos > 1:
            if pos % 2 == 0:   # second child → flips relative to parent
                flips += 1
            pos = (pos + 1) // 2
        # root is Engineer; each flip toggles
        return "Engineer" if flips % 2 == 0 else "Doctor"
