
# -------------------- Memoization (Top-Down DP) --------------------

def fibonacci(num, memo={}):
    if num in memo:
        return memo[num]

    if num <= 1:
        return num

    memo[num] = fibonacci(num - 1, memo) + fibonacci(num - 2, memo)
    return memo[num]


# Driver Code
num = int(input("Enter n: "))
result = fibonacci(num)
print("Fibonacci Number =", result)



# -------------------- Tabulation (Bottom-Up DP) --------------------

def fibonacci_tab(num):
    if num <= 1:
        return num

    dp = [0] * (num + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, num + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[num]


# Driver Code
num = int(input("Enter n: "))
answer = fibonacci_tab(num)
print("Fibonacci Number =", answer)


