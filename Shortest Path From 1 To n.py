class Solution:
    def minimumStep(self, n):

        steps = 0
        # work BACKWARDS from n to 1 (reverse the two forward moves):
        #   forward i -> 3*i   reverses as  n //= 3  (only when divisible by 3)
        #   forward i -> i+1   reverses as  n -= 1
        while n > 1:
            if n % 3 == 0:
                n //= 3        # big jump down -> always prefer when possible
            else:
                n -= 1         # otherwise step down by 1 toward a multiple of 3
            steps += 1

        return steps
