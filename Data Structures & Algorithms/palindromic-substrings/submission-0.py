class Solution:
    def countSubstrings(self, s: str) -> int:
        resp = 0
        for i in range(len(s)):
            resp += self.count(s, i, i)
            resp += self.count(s, i, i + 1)
        return resp

    def count(self, s, l, r):
        resp = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            resp += 1
            l -= 1
            r += 1
        return resp
        