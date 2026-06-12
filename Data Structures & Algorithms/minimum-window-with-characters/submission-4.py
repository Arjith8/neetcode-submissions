class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        track_t = {}
        for i in t:
            track_t[i] = track_t.get(i, 0) + 1
        
        left = 0
        track_s = {}
        to_complete = len(track_t)
        len_s = len(s)
        max_substring, max_substr_len = (0, -1), float("infinity")
        for right in range(len_s):
            current = s[right]
            if current in track_t:
                track_s[current] = track_s.get(current, 0) + 1
                if track_s[current] == track_t[current]:
                    to_complete -= 1
                
                while to_complete == 0:
                    length = right - left + 1
                    if length < max_substr_len:
                        max_substring = (left, right)
                        max_substr_len = length
                    
                    if s[left] in track_t:
                        track_s[s[left]] -= 1
                        if track_s[s[left]] < track_t[s[left]]:
                            to_complete += 1
                        
                    left += 1
        return s[max_substring[0]:max_substring[1]+1] 

            
        