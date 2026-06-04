class Solution:
    def countBits(self, n: int) -> List[int]:
        response = []
        for i in range(n+1):
            num_of_ones = 0
            num = i
            while num:
                num_of_ones += num%2
                num = num //2
            
            response.append(num_of_ones)

        return response

        
        