def unique_paths(m, n):
    # Create a 2D array to store the number of paths
    dp = [[0] * n for _ in range(m)]
    
    # Initialize the starting position
    for i in range(m):
        dp[i][0] = 1  # Only one way to reach any cell in the first column
    for j in range(n):
        dp[0][j] = 1  # Only one way to reach any cell in the first row
    
    # Fill the dp table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]  # Return the value at the bottom-right corner

# Example usage
m = 3  # Number of rows
n = 2  # Number of columns
result = unique_paths(m, n)
print(result)  # Output the number of unique paths