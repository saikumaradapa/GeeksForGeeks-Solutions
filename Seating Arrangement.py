class Solution:
    def canSeatAllPeople(self, k, seats):
        n = len(seats)
        for i in range(n):
            left = i > 0 and seats[i-1] == 1
            right = i < n - 1 and seats[i+1] == 1
            if seats[i] == 1:
                if left or right:
                    return False
            else:
                if not left and not right:
                    k -= 1
                    seats[i] = 1
        return k <= 0

'''
    greedy: scan left to right
    if occupied seat has adjacent occupied → invalid arrangement, return False
    if empty seat has no adjacent occupied → seat someone, mark it
    time complexity : O(n)
    space complexity : O(1)
'''
