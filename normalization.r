# Sample dataset
data <- c(10, 12, 15, 20, 25, 30, 35, 40, 50, 60)

# Min-Max Normalization
min_max_normalization <- function(x) {
  min_val <- min(x)
  max_val <- max(x)
  normalized <- (x - min_val) / (max_val - min_val)
  return(normalized)
}

# Z-score Normalization
z_score_normalization <- function(x) {
  mean_val <- mean(x)
  std_dev <- sd(x)
  normalized <- (x - mean_val) / std_dev
  return(normalized)
}

# MAD Normalization
mad_normalization <- function(x) {
  median_val <- median(x)
  mad_val <- mad(x)
  normalized <- (x - median_val) / mad_val
  return(normalized)
}

# Perform normalizations
min_max_norm <- min_max_normalization(data)
z_score_norm <- z_score_normalization(data)
mad_norm <- mad_normalization(data)

# Print results
cat("Original Data: ", data, "\n")
cat("Min-Max Normalization: ", min_max_norm, "\n")
cat("Z-score Normalization: ", z_score_norm, "\n")
cat("MAD Normalization: ", mad_norm, "\n")
