class Solution:
    def canServe(self, arr):
        five_count = 0
        ten_count = 0

        for bill in arr:
            if bill == 5:
                five_count += 1

            elif bill == 10:
                if five_count == 0:
                    return False
                five_count -= 1
                ten_count += 1

            else:  # bill == 20
                if ten_count > 0 and five_count > 0:
                    ten_count -= 1
                    five_count -= 1
                elif five_count >= 3:
                    five_count -= 3
                else:
                    return False

        return True

''' classic greedy problem
    time complexity : O(n)
    space complexity : O(1)
'''
