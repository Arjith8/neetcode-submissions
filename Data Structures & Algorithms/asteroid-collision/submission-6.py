class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            
            while stack and (i < 0 and stack[-1] > 0):
                diff = i + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff == 0:
                    stack.pop()
                    i = 0
                else:
                    i = 0
            if i:
                stack.append(i)

        return stack                    
        