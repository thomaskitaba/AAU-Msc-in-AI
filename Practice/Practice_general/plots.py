#!/usr/bin/python3
import matplotlib.pyplot as plt  # Importing matplotlib for visualization
print("Thomas Kitaba")
plt.ion()
# Step-2:- Prepare data 
x = [1, 2, 3, 4, 5]
y = ["a", "b", "c", "d", "f"]

z = [1, 2, 2, 3, 3, 3]

# Step-3:- Create a plot
# plt.plot(x, y, color="green", marker='o', markersize=10, linestyle='dashed', linewidth=2)  # Create a line plot with a green dashed line and red markers
plt.pie(x, labels=y)
plt.title("Simple Piechart")   # Add a title to the plot
plt.xlabel("Years")       # Add a label to the x-axis
plt.ylabel("Growth")      # Add a label to the y-axis

plt.ioff()
plt.show()
