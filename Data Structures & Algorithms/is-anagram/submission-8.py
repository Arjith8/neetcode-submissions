class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            (s, t) = (t, s)

        count_s = {}
        for i in s:
            count_s[i] = count_s.get(i, 0) + 1
        
        count_t = {}
        for i in t:
            count_t[i] = count_t.get(i, 0) + 1

        for key in count_t:
            if count_t.get(key, 0) != count_s.get(key, 0):
                return False
        
        return True
