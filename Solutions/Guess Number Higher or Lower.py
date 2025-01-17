# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

ANSWER = 42  
def guess(num: int) -> int:
    if num < ANSWER:
        return 1
    elif num > ANSWER:
        return -1
    else:
        return 0
    
class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            ###########################
            mid = (left + right) // 2 #
            ###########################
            result = guess(mid)
            if result == 0:  
                return mid
            elif result == 1:  
                left = mid + 1
            else:  
                right = mid - 1

solution = Solution()
n = 2**31 - 1
print("Guessed number:", solution.guessNumber(n))