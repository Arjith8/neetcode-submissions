class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest_string = strs[0]
        for i in strs:
            if len(i) < len(smallest_string):
                smallest_string = i
        c = 0
        for i in range(len(smallest_string)):
            for j in strs:
                if smallest_string[i] != j[i]:
                    return smallest_string[:c]
            else:
                c+=1
        return smallest_string

        