class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def ways_to_climb(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            elif n == 2:
                return 2


            if n in memo:
                return memo[n]
            memo[n] = ways_to_climb(n-2) + ways_to_climb(n-1)

            return memo[n]  
        return ways_to_climb(n)