#192211059
# Load the mtcars dataset
data("mtcars")

# Create the boxplot
boxplot(mpg ~ as.factor(cyl), data = mtcars,
        main = "Boxplot of MPG by Number of Cylinders",
        xlab = "Number of Cylinders",
        ylab = "Miles Per Gallon (MPG)",
        col = "lightblue",
        border = "darkblue")

# Add a legend
legend("topright", legend = levels(as.factor(mtcars$cyl)), 
       title = "Number of Cylinders", fill = "lightblue", border = "darkblue")
