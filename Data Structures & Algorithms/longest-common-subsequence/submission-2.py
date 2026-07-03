class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        track = {}
        def dfs(i, j):
            print(i, j)
            if (i, j) in track:
                return track[(i,j)]
            if i == len(text1) or j == len(text2):
                longest_seq_len = 0
            elif text1[i] == text2[j]:
                longest_seq_len = 1 + dfs(i + 1, j + 1)
            else:
                longest_seq_len = max(dfs(i + 1, j), dfs(i, j + 1))

            track[(i,j)] = longest_seq_len
            return longest_seq_len

        return dfs(0, 0)
