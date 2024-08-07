#192211059
# Load necessary libraries
library(ggplot2)
library(dplyr)

# Load the dataset from a CSV file
diabetes <- read.csv("C:\Users\ramya\OneDrive\Documents\DAY 2\diabetes.csv")

# Check the structure of the dataset
str(diabetes)

# Create a scatterplot of BloodPressure vs Age
ggplot(diabetes, aes(x = Age, y = BloodPressure)) +
  geom_point(color = "blue") +
  labs(title = "Scatterplot of Blood Pressure vs Age",
       x = "Age",
       y = "Blood Pressure") +
  theme_minimal()

# Define age groups
diabetes <- diabetes %>%
  mutate(AgeGroup = cut(Age, breaks = seq(0, 100, by = 10),
                        labels = paste(seq(0, 90, by = 10), seq(10, 100, by = 10), sep = "-"),
                        right = FALSE))

# Calculate average Blood Pressure for each Age Group
avg_bp_by_age_group <- diabetes %>%
  group_by(AgeGroup) %>%
  summarise(AverageBloodPressure = mean(BloodPressure, na.rm = TRUE))

# Create a bar chart of average Blood Pressure by Age Group
ggplot(avg_bp_by_age_group, aes(x = AgeGroup, y = AverageBloodPressure, fill = AgeGroup)) +
  geom_bar(stat = "identity") +
  labs(title = "Average Blood Pressure by Age Group",
       x = "Age Group",
       y = "Average Blood Pressure") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
