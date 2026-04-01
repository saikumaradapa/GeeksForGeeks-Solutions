class Solution:
	def countStrings(self,n):
	    dp = dict()
    	def dfs(i, prev_bit):
    	    if i == n:
    	        return 1
    	    if (i, prev_bit) in dp: return dp[(i, prev_bit)]
    	    
    	    dp[(i, prev_bit)] = dfs(i+1, 0)
    	    
    	    if prev_bit == 0:
    	        dp[(i, prev_bit)] += dfs(i+1, 1)
    	    
    	    return dp[(i, prev_bit)]
    	return dfs(0, 0)
    	    
