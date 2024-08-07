#192211059
find_median <- function(values) {
  sorted_values <- sort(values)
  n <- length(sorted_values)
  
  if (n %% 2 == 1) {
    
    median <- sorted_values[(n + 1) / 2]
  } else {
    
    median <- (sorted_values[n / 2] + sorted_values[(n / 2) + 1]) / 2
  }
  
  return(median)
}

values <- c(200,450,300,1500,700,44)
age <- c(5,15,20,50,80,110)
median_value <- find_median(values)
median_value1 <- find_median(age)
cat("The median is:", median_value)
cat("The median is:", median_value1)