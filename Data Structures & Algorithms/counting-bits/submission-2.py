class Solution:
    def countBits(self, n: int) -> List[int]:
        response = [0] * (n+1)

        most_significant_bit_value = 1
        for i in range(1, n+1):
            if i == most_significant_bit_value * 2:
                most_significant_bit_value = i
            num_of_ones = response[i - most_significant_bit_value] + 1
            response[i] = num_of_ones

        return response

        
        