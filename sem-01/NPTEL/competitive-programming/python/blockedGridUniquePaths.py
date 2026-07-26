def unique_paths_with_obstacles(obstacle_grid):
    if not obstacle_grid or obstacle_grid[0][0] == 1 or obstacle_grid[-1][-1] == 1:
        return 0  # Return 0 if start or end is blocked
    
    m, n = len(obstacle_grid), len(obstacle_grid[0])
    dp = [[0] * n for _ in range(m)]
    
    # Initialize the starting position
    dp[0][0] = 1  # Start position
    
    # Fill the dp table
    for i in range(m):
        for j in range(n):
            if obstacle_grid[i][j] == 1:  # If there's an obstacle
                dp[i][j] = 0
            else:
                if i > 0:
                    dp[i][j] += dp[i-1][j]  # Paths from above
                if j > 0:
                    dp[i][j] += dp[i][j-1]  # Paths from left
    
    return dp[m-1][n-1]  # Return the value at the bottom-right corner

# Example usage
obstacle_grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
result = unique_paths_with_obstacles(obstacle_grid)
print(result)  # Output the number of unique paths
