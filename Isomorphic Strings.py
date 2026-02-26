class Solution:
    def areIsomorphic(self, s1, s2):
        if len(s1) != len(s2):
            return False
        
        keys, values = dict(), dict()
        for i in range(len(s1)):
            if s1[i] not in keys and s2[i] not in values:
                keys[s1[i]] = s2[i]
                values[s2[i]] = s1[i]
            elif (s1[i] not in keys and s2[i] in values) or (s1[i] in keys and s2[i] not in values) or (keys[s1[i]] != s2[i] or values[s2[i]] != s1[i]):
                return False
                

        return True
