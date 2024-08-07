#192211059
# Data
data <- c(1, 1, 5, 5, 5, 5, 5, 8, 8, 10, 10, 10, 10, 12, 14, 14, 14, 15, 15, 15, 15, 15, 15, 18, 18, 18, 18, 18, 18, 18, 
          20, 20, 20, 20, 20, 20, 20, 21, 21, 21, 21, 25, 25, 25, 25, 25, 28, 28, 30)

# Number of bins
k <- 3

# Equal-frequency partitioning
n <- length(data)
bin_size <- ceiling(n / k)
bins <- split(data, ceiling(seq_along(data) / bin_size))

# Smoothing by bin means
bin_means <- sapply(bins, mean)
smoothed_by_means <- unlist(lapply(1:length(bins), function(i) rep(bin_means[i], length(bins[[i]]))))

# Smoothing by bin boundaries
smoothed_by_boundaries <- unlist(lapply(bins, function(bin) {
  c(rep(min(bin), floor(length(bin) / 2)), rep(max(bin), ceiling(length(bin) / 2)))
}))

# Plotting histograms
par(mfrow=c(3, 1))

# Original data histogram
hist(data, breaks=15, main='Original Data Histogram', xlab='Price', ylab='Frequency', col='blue')

# Smoothed by bin means histogram
hist(smoothed_by_means, breaks=15, main='Data Smoothed by Bin Means', xlab='Price', ylab='Frequency', col='green')

# Smoothed by bin boundaries histogram
hist(smoothed_by_boundaries, breaks=15, main='Data Smoothed by Bin Boundaries', xlab='Price', ylab='Frequency', col='red')
