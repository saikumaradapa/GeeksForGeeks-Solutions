class Solution:
    def generateUsernames(self, arr: list[str]) -> list[str]:

        reserved = set(arr)      # every input name is reserved up front
        used = set()             # names already assigned
        next_k = {}              # base name -> next suffix to try
        res = []

        for name in arr:
            if name not in used:
                # first time this name is assigned -> keep it
                used.add(name)
                res.append(name)
            else:
                k = next_k.get(name, 1)
                # smallest suffix not reserved and not already assigned
                while (name + str(k)) in reserved or (name + str(k)) in used:
                    k += 1
                cand = name + str(k)
                used.add(cand)
                res.append(cand)
                next_k[name] = k + 1    # later duplicates start after this

        return res
