class Solution:
    def isProduct(self, arr, target):
        numSet = set()
        for n in arr:
            if n != 0 and target % n == 0 and (target // n) in numSet:
                return True
            if n == 0 and target == 0 and numSet:
                return True
            numSet.add(n)
        return False

'''
    for each element n, check if target/n exists in seen set
    use integer division with modulo check to avoid float issues
    handle zero case: 0 * any_previous = 0
    time complexity : O(n)
    space complexity : O(n)
'''
