#192211059
# Example dataset of tennis scores
scores <- c(10, 12, 15, 14, 16, 20, 22, 19, 25, 24, 30, 50)
# Create a boxplot for tennis scores
boxplot(scores, 
        main = "Boxplot of Tennis Scores",
        ylab = "Scores",
        col = "lightgreen",
        border = "blue",
        horizontal = FALSE)

# Add a grid for better visualization
grid()