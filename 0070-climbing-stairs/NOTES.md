# How to solve
##### 1. jot down random ideas
1. setting variables
- step = [1, 2], allowed to use same steps more than twice.
- ways = (ways_to_climb)
  
#### 2. 📕 Recursive function: to find out if it's asking to use recursive function, you need to find the pattern.
- n = 0, ways = 0 <- Q. There is no way to climb 0 stairs, but why can it be set as 1 according to the solution?
- n = 1, ways = 1
- n = 2, ways = 2 (1+1 / 2)
- n = 3, ways = 3 (1+1+1 / 1+2 / 2+1)
- n = 4, ways = 5 (1+1+1+1 / 1+1+2 / 1+2+1 / 2+1+1 / 2+2)
- n = 5, ways = 8 (1+1+1+1+1 / 1+1+1+2 / 1+1+2+1 / 1+2+1+1 / 2+1+1+1 / 2+2+1 / 2+1+2 / 1+2+2)
- => ***Same with Fibonacci!***

# 📕 To memorize
##### 1. Recursive function: "routine that calls itself directly or indirectly - geeksforgeeks"
##### 2. Memoization: keeps the result in **dictionary** so that the computer doesn't have to calculate it repeatedly. (Note: it should be dictionary to allow access by keys)
- changes in code compared to recursion
'''
    else:
        return ways_to_climb(n-2) + ways_to_climb(n-1)
'''
'''
    if n in memo:
        return memo[n]
    memo[n] = ways_to_climb(n-2) + ways_to_climb(n-1)
'''
