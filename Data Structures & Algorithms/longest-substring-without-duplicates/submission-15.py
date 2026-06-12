class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        track = {}
        max_len = 0
        for right in range(len(s)):
            if s[right] in track:
                while s[right] in track:
                    track.pop(s[left])
                    left += 1
                    
            track[s[right]] = 1
            max_len = max(max_len, right - left + 1)
        
        return max_len