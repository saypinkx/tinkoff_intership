def find_combination(n, m, a):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for j in range(1, m + 1):
        dp[0][j] = 0
    for i in range(1, n + 1):
        dp[i][0] = -1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[j - 1] <= i and dp[i - a[j - 1]][j - 1] != -1:
                dp[i][j] = dp[i - a[j - 1]][j - 1] + 1
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp)
    if dp[n][m] == -1:
        return -1

    combination = []
    i = n
    j = m

    while i > 0 and j > 0:
        if dp[i][j] <= dp[i][j - 1]:
            j -= 1
        else:
            combination.append(a[j - 1])
            i -= a[j - 1]

    return len(combination), combination[::-1]


n, m = map(int, input().split())
a = list(map(int, input().split()))

k, result = find_combination(n, m, a)
if k == -1:
    print(-1)
else:
    print(k)
    print(*result)