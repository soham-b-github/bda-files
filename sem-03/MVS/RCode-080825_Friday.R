# Load necessary library
library(MASS)
library(ggplot2)
library(ellipse)

# Step 1: Set parameters and generate samples
set.seed(123)  # For reproducibility
n_samples <- 1000
mu <- c(0, 0)
sigma <- matrix(c(1, 0.7, 0.7, 1), nrow = 2)

# Generate samples from bivariate normal
samples <- mvrnorm(n = n_samples, mu = mu, Sigma = sigma)

# Step 2: Compute Mahalanobis distances
# Mahalanobis distance from mean
mahal_distances <- mahalanobis(samples, center = mu, cov = sigma)

# Step 3: Find 95th percentile of chi-square distribution with df = 2
threshold <- qchisq(0.95, df = 2)

# Step 4: Count how many distances exceed the threshold
num_exceeding <- sum(mahal_distances > threshold)

# Output the result
cat("Number of samples with Mahalanobis distance > 95th percentile (chisq):", num_exceeding, "\n")

# Creating dataframes for the samples drawn
samples_df <- as.data.frame(samples)
colnames(samples_df) <- c("X1", "X2")

# Add a column indicating whether each point exceeds the threshold
samples_df$Exceeds <- mahal_distances > threshold

# Step 5: Plot the distribution with 95% ellipse
# Create the ellipse for 95% confidence region
ellipse_95 <- as.data.frame(ellipse(sigma, centre = mu, level = 0.95))

# Plot using ggplot2
ggplot(samples_df, aes(x = X1, y = X2)) +
  geom_point(aes(color = Exceeds), alpha = 0.6) +
  scale_color_manual(values = c("FALSE" = "blue", "TRUE" = "red"),
                     labels = c("Within 95%", "Outside 95%"),
                     name = "Mahalanobis\nDistance") +
  geom_path(data = ellipse_95, aes(x = x, y = y), color = "black", size = 1, linetype = "dashed") +
  labs(title = "Bivariate Normal Sample with 95% Mahalanobis Distance Ellipse",
       x = "X1", y = "X2") +
  theme_minimal()
