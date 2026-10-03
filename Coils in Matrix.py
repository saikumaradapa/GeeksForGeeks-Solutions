class Solution:
    def formCoils(self, n: int) -> list[list[int]]:

        S = 4 * n                      # matrix side length

        def val(r, c):
            return r * S + c + 1       # row-major value at (r, c)

        # step-length pattern for the inward spiral:
        #   S-1, then (S-2, S-2), (S-4, S-4), (S-6, S-6), ...
        steps = [S - 1]
        dec = S - 2
        while dec > 0:
            steps.append(dec)
            steps.append(dec)
            dec -= 2

        def build(start_r, start_c, dirs):
            r, c = start_r, start_c
            coil = [val(r, c)]
            di = 0
            for st in steps:
                dr, dc = dirs[di % 4]
                for _ in range(st):
                    r += dr
                    c += dc
                    coil.append(val(r, c))
                di += 1
            return coil

        D, R, U, L = (1, 0), (0, 1), (-1, 0), (0, -1)

        # coil 1: start top-left (0,0), turn order Down -> Right -> Up -> Left
        coil1 = build(0, 0, [D, R, U, L])
        # coil 2: start bottom-right (S-1,S-1), opposite turn order Up -> Left -> Down -> Right
        coil2 = build(S - 1, S - 1, [U, L, D, R])

        return [coil1, coil2]

