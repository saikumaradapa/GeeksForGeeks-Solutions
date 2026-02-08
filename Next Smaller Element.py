class Solution:
	def nextSmallerEle(self, arr):
		res = [-1] * len(arr)
		n = len(arr)
		
		stack = []
		for i in range(n-1, -1, -1):
		    while stack and stack[-1] >= arr[i]:
		        stack.pop()
		    
		    res[i] = stack[-1] if stack else -1
		    stack.append(arr[i])
		 
        return res

''' monotonic max stack
    time complexity : O(n)
    space complexity : O(1)
'''
