#192211059
# Data for Class A and Class B
class_A <- c(76, 35, 47, 64, 95, 66, 89, 36, 84)
class_B <- c(51, 56, 84, 60, 59, 70, 63, 66, 50)

# Calculate mean, median, and range for Class A
mean_A <- mean(class_A)
median_A <- median(class_A)
range_A <- range(class_A)
range_A_diff <- range_A[2] - range_A[1]

# Calculate mean, median, and range for Class B
mean_B <- mean(class_B)
median_B <- median(class_B)
range_B <- range(class_B)
range_B_diff <- range_B[2] - range_B[1]

# Print the results
print(paste("Class A - Mean:", mean_A, "Median:", median_A, "Range:", range_A_diff))
print(paste("Class B - Mean:", mean_B, "Median:", median_B, "Range:", range_B_diff))

# Create a data frame for boxplot
data <- data.frame(
  scores = c(class_A, class_B),
  class = factor(c(rep("Class A", length(class_A)), rep("Class B", length(class_B))))
)

# Plot boxplot
boxplot(scores ~ class, data = data, main = "Scores by Class", ylab = "Scores", col = c("lightblue", "lightgreen"))

# Inferences
# Based on the boxplot, we can observe the distribution of scores, the median, the quartiles, and any potential outliers.
