def count_ways_to_sum(n):
    # Create a DP array to store the number of ways to get each sum
    dp = [0] * (n + 1)
    
    # Base case
    dp[0] = 1  # One way to make 0 (by not rolling)
    
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, 7):  # Dice values from 1 to 6
            if i - j >= 0:
                dp[i] += dp[i - j]

    return dp[n]

# Example usage
sum_target = 10
result = count_ways_to_sum(sum_target)
print(result)  # Output the number of unique ways to construct the sum of 10
