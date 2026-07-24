class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        min_rate = right
        while left <= right:
            print(left , right)
            middle = left + (right - left)//2
            time_taken = 0
            for i in piles:
                time_taken += i // middle
                if i % middle != 0:
                    time_taken += 1
            print("kkk", middle, time_taken, min_rate)
            if time_taken <= h:
                print("kk", min_rate, middle)
                min_rate = min(min_rate, middle)
                right = middle - 1
            
            else:
                left = middle + 1
        
        return min_rate   

        