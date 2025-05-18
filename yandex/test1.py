# def three_points_in_row(n: int):
#     n = int(input())
#     dp = [0] * (n + 4)

#     dp[1], dp[2], dp[3] = 2, 4, 7
#     for i in range(4, n + 1):
#         dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 12345

#     return dp[n]

def three_points_in_row(n: int):
    dp = [0, 2, 4, 7]
    dp.extend([0 for i in range(n - 3)])
    for i in range(4, n + 1):
        next_digit = dp[i - 3] + dp[i - 2] + dp[i - 1]
        dp[i] = next_digit
    return dp[n]



print(three_points_in_row(int(input())))