def knapsack(expenses, budget):
    n = len(expenses)

 
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]


    for i in range(1, n + 1):
        name, cost, value = expenses[i - 1]

        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(
                    value + dp[i - 1][w - cost],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]


    res = []
    w = budget

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name, cost, value = expenses[i - 1]
            res.append((name, cost))
            w -= cost

    return res[::-1], dp[n][budget]
