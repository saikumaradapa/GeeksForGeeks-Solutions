class Solution:
    def countVowels(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        m = len(queries)
        vowels_cnt = [0] * n
        
        vowels_set = {'a', 'e', 'i', 'o', 'u'}
        current_vowel_cnt = 0 
        for i in range(n):
            if s[i] in vowels_set:
                current_vowel_cnt += 1
            vowels_cnt[i] = current_vowel_cnt

        ans = [0] * m
        for i in range(m):
            l, r = queries[i]
            ans[i] = vowels_cnt[r] - vowels_cnt[l - 1] if l > 0 else vowels_cnt[r]
        return ans
        
