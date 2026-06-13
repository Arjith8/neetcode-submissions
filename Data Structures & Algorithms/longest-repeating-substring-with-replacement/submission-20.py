class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        left = 0
        max_freq = 0
        track = {}
        for right in range(len(s)):
            track[s[right]] = track.get(s[right], 0) + 1
            max_freq = max(track[s[right]], max_freq)
            length = right - left + 1
            # check if num of repacements we have is appropriate wrt k
            # print(track)
            while length - max_freq - k > 0:
                track[s[left]] -= 1
                left += 1
                length -= 1
                max_freq = max(max_freq, track[s[left]])
                pass
            print(track)

            max_len = max(max_len, length)

        return max_len
        