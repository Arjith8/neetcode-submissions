class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ""
        longest_pallindrome_len = 0
        for i in range(len(s)):
            for j in range(i, len(s)+1):
                substr = s[i:j]
                if substr == substr[::-1]:
                    if longest_pallindrome_len < (j - i):
                        longest_pallindrome_len = (j - i)
                        longest_palindrome = substr
        
        return longest_palindrome