library(ggplot2)
data = read.csv("Data2.csv",header=FALSE)

data
colnames(data) = c("Index","Language","Country")
head(data)

language_count = table(data$Language, data$Country)
language_df = as.data.frame(language_count)

language_df
colnames(language_df) = c("Language","Country","Freq")

# Hobe na eta karon eta purotar respect e thakbe
# language_percent = language_df
# language_percent[,-1] = language_percent[,-1]/rowSums(language_percent[,-1])*100

# Install and load the tidyr package if you haven't already
install.packages("tidyr")
library(tidyr)

# Reshape the data into wide format
language_wide <- spread(language_df, key = Language, value = Freq, fill = 0)

# Check the reshaped data
head(language_wide)

# Normalize the data to percentages
language_wide_percent <- language_wide
language_wide_percent[ , -1] <- language_wide_percent[ , -1] / rowSums(language_wide_percent[ , -1]) * 100

# Check the normalized data
head(language_wide_percent)

# Reshape data into long format for ggplot2
language_long <- gather(language_wide_percent, key = "Language", value = "Percentage", -Country)
language_long

# Create the 100% stacked bar chart
ggplot(language_long, aes(x = Country, y = Percentage, fill = Language)) +
  geom_bar(stat = "identity") +
  ylab("Percentage") +
  xlab("Country") +
  ggtitle("100% Stacked Bar Chart of Languages by Country") +
  theme(axis.text.x = element_text(angle = 90, hjust = 1))
