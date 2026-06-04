class Solution:
    def reverseBits(self, n: int) -> int:
        response = 0
        for i in range(32):
            if n % 2:
                response = (1 << (31 - i)) | response
            n = n >> 1
        return response


        