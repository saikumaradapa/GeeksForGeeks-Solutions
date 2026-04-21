class Solution:
    def minSteps(self, m, n, d):
        from math import gcd
        
        # Check feasibility
        if d > max(m, n) or d % gcd(m, n) != 0:
            return -1
        
        # Helper to simulate pouring from "fromJug" to "toJug"
        def pour(fromJug, toJug):
            from_curr = fromJug  # fill source
            to_curr = 0
            step = 1  # first fill
            
            while from_curr != d and to_curr != d:
                # pour water
                temp = min(from_curr, toJug - to_curr)
                to_curr += temp
                from_curr -= temp
                step += 1
                
                if from_curr == d or to_curr == d:
                    break
                
                # if source becomes empty → fill again
                if from_curr == 0:
                    from_curr = fromJug
                    step += 1
                
                # if destination becomes full → empty it
                if to_curr == toJug:
                    to_curr = 0
                    step += 1
            
            return step
        
        # Try both directions
        return min(pour(m, n), pour(n, m))
