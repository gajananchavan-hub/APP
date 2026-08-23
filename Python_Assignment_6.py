def knapsack_bottom_up(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


def knapsack_top_down(weights, values, n, capacity, dp):
    if n == 0 or capacity == 0:
        return 0

    if dp[n][capacity] != -1:
        return dp[n][capacity]

    if weights[n - 1] <= capacity:
        include = values[n - 1] + knapsack_top_down(
            weights, values, n - 1,
            capacity - weights[n - 1], dp
        )
        exclude = knapsack_top_down(
            weights, values, n - 1, capacity, dp
        )
        dp[n][capacity] = max(include, exclude)
    else:
        dp[n][capacity] = knapsack_top_down(
            weights, values, n - 1, capacity, dp
        )

    return dp[n][capacity]


weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

n = len(weights)

bottom_up_result = knapsack_bottom_up(weights, values, capacity)

dp = [[-1] * (capacity + 1) for _ in range(n + 1)]
top_down_result = knapsack_top_down(weights, values, n, capacity, dp)

print("Bottom-Up Result:", bottom_up_result)
print("Top-Down Result:", top_down_result)
