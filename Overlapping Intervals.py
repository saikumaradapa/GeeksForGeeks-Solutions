class Solution:
	def mergeOverlap(self, arr):
		arr.sort()
		res = [[arr[0][0], arr[0][1]]]
		
		for start, end in arr[1:]:
		    last = res[-1][1]
		    
		    if start <= last:
		        res[-1][1] = max(last, end)
            else:
                res.append([start, end])
        
        return res

''' 
    time complexity : O(n logn)
    space complexity : O(1)
'''
