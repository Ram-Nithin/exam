# Sample data
data <- c(5, 6, 7, 8, 12, 15, 19, 22, 25, 28)

# Define the number of bins
n_bins <- 3

# Cut the data into bins
bins <- cut(data, breaks = n_bins, include.lowest = TRUE)

# Calculate bin means
bin_means <- tapply(data, bins, mean)
data_bin_means <- as.numeric(bin_means[as.factor(bins)])

# Calculate bin medians
bin_medians <- tapply(data, bins, median)
data_bin_medians <- as.numeric(bin_medians[as.factor(bins)])

# Calculate bin boundaries
replace_with_boundary <- function(values) {
  min_val <- min(values)
  max_val <- max(values)
  sapply(values, function(x) ifelse(abs(x - min_val) < abs(x - max_val), min_val, max_val))
}

data_bin_boundaries <- unlist(tapply(data, bins, replace_with_boundary))

# Output the results
cat("Original Data:\n", data, "\n\n")
cat("Binned by Means:\n", data_bin_means, "\n\n")
cat("Binned by Medians:\n", data_bin_medians, "\n\n")
cat("Binned by Boundaries:\n", data_bin_boundaries, "\n")
