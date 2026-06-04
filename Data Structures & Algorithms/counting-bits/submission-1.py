class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        response = [0, 1]

        most_significant_bit_value = 2
        for i in range(2, n+1):
            if i == most_significant_bit_value * 2:
                most_significant_bit_value = i
            num_of_ones = response[i - most_significant_bit_value] + 1
            response.append(num_of_ones)

        return response

        
        