class Solution:
    def findTwoElement(self, arr):
        n = len(arr)
        xor_sum = 0
        
        # Step 1: XOR all elements and numbers from 1 to n
        for i in range(n):
            xor_sum ^= arr[i]
            xor_sum ^= (i + 1)
        
        # Step 2: Find rightmost set bit
        bitNo = 0
        while (xor_sum & (1 << bitNo)) == 0:
            bitNo += 1
        
        bucket0, bucket1 = 0, 0
        
        # Step 3: Divide into two buckets based on the set bit
        for i in range(n):
            if arr[i] & (1 << bitNo):
                bucket1 ^= arr[i]
            else:
                bucket0 ^= arr[i]
            if (i + 1) & (1 << bitNo):
                bucket1 ^= (i + 1)
            else:
                bucket0 ^= (i + 1)
        
        # Step 4: Check which is missing and which is repeated
        cnt = arr.count(bucket1)  # More readable than manual count
        if cnt == 2:
            return [bucket1, bucket0]  # [repeated, missing]
        else:
            return [bucket0, bucket1]  # [repeated, missing]


''' bit manipulation approach 
    time complexity : O(n)
    space complexity : O(1)
'''
