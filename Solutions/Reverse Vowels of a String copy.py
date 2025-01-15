class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for asteroid in asteroids:
            # at least on ast exists, ast minus, stack[-1] plus
            while stack and asteroid < 0 < stack[-1]:  
                if abs(asteroid) > stack[-1]:  
                    stack.pop()
                elif abs(asteroid) == stack[-1]: 
                    stack.pop()
                    break
                else: 
                    break
            else:
                stack.append(asteroid)
        return stack

s = Solution()
print(s.asteroidCollision([-10,2,5]))