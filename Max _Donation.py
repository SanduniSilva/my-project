def calculate_max_donations(don_list):
    don_amount = list(map(int, don_list.split()))
    n = len(don_amount)

    if n == 1:
        return don_amount[0]

    dp = [0] * n
    dp[0] = don_amount[0]
    dp[1] = max(don_amount[0], don_amount[1])

    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + don_amount[i])

    return max(dp[-1], dp[-2])

don_list = input("Input : ")
max_amount = calculate_max_donations(don_list)
print("Output:", max_amount)


