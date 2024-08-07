#192211059
# Load the mtcars dataset
data("mtcars")

# Plot mpg and qsec as multiple lines in a single plot
# We will use the 'matplot' function which is designed for such purposes
matplot(mtcars[, c("mpg", "qsec")], type = "o", pch = 1, col = c("blue", "red"), 
        xlab = "Car Index", ylab = "Values", main = "MPG and QSEC of mtcars")

# Add a legend to the plot
legend("topright", legend = c("MPG", "QSEC"), col = c("blue", "red"), pch = 1, lty = 1)