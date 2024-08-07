#192211059
# Given data
data <- c(200, 300, 400, 600, 1000)

# Min-Max Normalization
min_val <- min(data)
max_val <- max(data)
min_max_normalized <- (data - min_val) / (max_val - min_val)

# Print the normalized data
print(min_max_normalized)
# Given data
data <- c(200, 300, 400, 600, 1000)

# Z-Score Normalization
mean_val <- mean(data)
sd_val <- sd(data)
z_score_normalized <- (data - mean_val) / sd_val

# Print the normalized data
print(z_score_normalized)
