class Solution:
    def findPreSuc(self, root, key):
        predecessor = None
        successor = None
        
        curr = root
        
        while curr:
            if curr.data < key:
                predecessor = curr
                curr = curr.right
            elif curr.data > key:
                successor = curr
                curr = curr.left
            else:
                # If key found
                
                # Find max in left subtree
                temp = curr.left
                while temp:
                    predecessor = temp
                    temp = temp.right
                
                # Find min in right subtree
                temp = curr.right
                while temp:
                    successor = temp
                    temp = temp.left
                
                break
        
        return [predecessor, successor]


''' 
    time complexity : O(log n)
    space complexity : O(1)
'''
