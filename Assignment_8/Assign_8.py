"""
Assignment (28/02/2026)

Assignment Name : Storytelling with Graphs
Description : Create bar chart, pie chart, histogram and write a short data story explaining trends.

This program creates different types of graphs such as bar chart, pie chart, and histogram using matplotlib. These graphs help in visualizing data and understanding patterns, distribution, and comparisons between categories.

Data Story:
The bar chart shows that category B has the highest value, indicating it performs better than others. The pie chart highlights the proportion of each category, where B occupies the largest share. The histogram shows the distribution of values, where most data points are concentrated around the middle range. Overall, the data suggests that certain categories dominate while others have moderate or lower performance

"""



import matplotlib.pyplot as plt

# Sample data
categories = ['A', 'B', 'C', 'D']
values = [20, 35, 25, 20]

# Bar Chart
plt.figure()
plt.bar(categories, values)
plt.title("Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# Pie Chart
plt.figure()
plt.pie(values, labels=categories, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()

# Histogram
data = [10, 20, 20, 30, 40, 40, 40, 50, 60]

plt.figure()
plt.hist(data)
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

