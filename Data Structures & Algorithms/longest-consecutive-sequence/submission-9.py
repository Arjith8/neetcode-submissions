class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        track = {}
        for i in nums:
            track[i] = 1
        
        longest_sequence = 0
        for i in track:
            length = track[i]
            while track.get(i + length, 0):
                temp = track[i + length]
                track[i + length] = 0
                length += temp
                track[i] = length
            longest_sequence = max(longest_sequence, length)
        
        return longest_sequence
