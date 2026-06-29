class Solution:
    def countSubstrings(self, s: str) -> int:
        resp = 0
        def check_for_palindrome(left, right):
            nonlocal resp
            if left < 0 or right >= len(s) or s[left] != s[right]:
                return
            
            resp += 1
            check_for_palindrome(left-1, right+1)
            
        
        for i in range(len(s)):
            check_for_palindrome(i, i)
            check_for_palindrome(i, i+1)
        
        return resp

        