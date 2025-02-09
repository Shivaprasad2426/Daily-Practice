# Load necessary libraries
library(ggplot2)
library(dplyr)

# Generate sample data
set.seed(42)
data <- data.frame(
  x = rnorm(1000),
  y = rnorm(1000)
)

# Data transformation
data <- data %>%
  mutate(
    z = x + y,
    category = ifelse(z > 1, "A", "B")
  )

# Plot the data
ggplot(data, aes(x = x, y = y, color = category)) +
  geom_point() +
  theme_minimal() +
  labs(
    title = "Scatter Plot of Sample Data",
    x = "X Axis",
    y = "Y Axis"
  )

# Save the plot
ggsave("scatter_plot.png")

# Additional analysis
summary_stats <- data %>%
  group_by(category) %>%
  summarise(
    mean_x = mean(x),
    mean_y = mean(y),
    mean_z = mean(z),
    sd_x = sd(x),
    sd_y = sd(y),
    sd_z = sd(z)
  )

print(summary_stats)

# Save the summary statistics to a CSV file
write.csv(summary_stats, "summary_stats.csv", row.names = FALSE)