from functools import cmp_to_key

class Solution:
    def findLargest(self, arr):
        
        arr = list(map(str, arr))
        
        # Custom comparator
        def compare(a, b):
            if a + b > b + a:
                return -1   # a should come first
            elif a + b < b + a:
                return 1    # b should come first
            else:
                return 0
        
        arr.sort(key=cmp_to_key(compare))
        
        result = ''.join(arr)
        
        return "0" if result[0] == '0' else result
