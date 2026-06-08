class Solution:


    def encode(self, strs: List[str]) -> str:
        temp = []
        for i in strs:
            temp.append(str(len(i)))
            temp.append('#')
            temp.append(i)
        return "".join(temp)


    def decode(self, s: str) -> List[str]:
        i = 0
        prev_string_end = 0
        resp = []
        while i < len(s):
            if s[i] == '#':
                length = int(s[prev_string_end:i])
                start = i + 1
                end = start + length
                resp.append(s[start:end])
                i = prev_string_end = end
                continue
            i += 1
        return resp
