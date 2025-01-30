# Create sample data
fruits <- c("Apple", "Orange", "Banana", "Grape")

quantity <- c(10, 5, 8, 12)


# Create a data frame
fruit_data <- data.frame(Fruit = fruits, Quantity = quantity)



# Plot a bar chart
barplot(Quantity ~ Fruit, data = fruit_data, xlab = "Fruit", ylab = "Quantity", main = "Fruit Quantity")
