class Solution:
    def maxValue(self, n: int) -> int:

        if n == 0:
            return 0

        bits = bin(n)[2:]        # binary string, most-significant bit first
        res = []
        run = 0                  # current count of consecutive set bits kept

        for b in bits:
            if b == '1':
                run += 1
                if run == 3:
                    res.append('0')   # clear this bit to break "111"
                    run = 0           # reset the consecutive-1 counter
                else:
                    res.append('1')   # keep it (run is 1 or 2)
            else:
                res.append('0')
                run = 0               # a 0 resets the run

        return int(''.join(res), 2)
