class Solution:
    def nthCharacter(self, n):

        digits = 1        # digit length of numbers in the current block
        count = 9         # how many numbers are in this block
        start = 1         # first number in this block

        # skip whole blocks while n lies past them
        while n > digits * count:
            n -= digits * count
            digits += 1
            count *= 10
            start *= 10

        # n is now a 1-based position inside the current block
        num = start + (n - 1) // digits      # the number that holds the nth char
        idx = (n - 1) % digits               # which digit of that number
        return str(num)[idx]
