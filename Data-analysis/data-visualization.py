import matplotlib.pyplot as plt

##############################################################
##############################################################
#   BASIC PLOTTING
##############################################################
##############################################################
x = [1,2,3,4,5]
y = [10,20,30,40,50]
# create the plot
plt.plot(x,y,color='red', marker='o', linestyle='--', linewidth=2)

# adding title and label
plt.title('Basic Plotting')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# adding grid
plt.grid(True)

# show the plot
# plt.show()

# Common Markers:
# 'o' – Circle
# 's' – Square
# '*' – Star
# 'd' – Diamond
# Line Styles:
# '-' – Solid Line
# '--' – Dashed Line
# ':' – Dotted Line

#######################################################
#######################################################
# BAR CHARTS
#######################################################
#######################################################
# vertical bar chart
categories = ['A','B','C','D','E']
values = [1,2,3,4,5]
plt.bar(categories,values, color='purple')
plt.title('Bar charts')
plt.xlabel('Categories')
plt.ylabel('Values')
# plt.show()

# Horizontal Bar chart
plt.barh(categories,values,color='blue')
plt.title('Horizonatl bar chart')
plt.show()

#########################################################
#########################################################
# SCATTER PLOT
#########################################################
#########################################################
import numpy as np

# Generating random data
x = np.random.rand(50)
y = np.random.rand(50)

# Scatter plot
plt.scatter(x, y, color='green', marker='x')

# Titles and labels
plt.title("Scatter Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Show the plot
plt.show()

##########################################################
##########################################################
# HISTOGRAM
##########################################################
##########################################################
data = np.random.randn(1000)  # Generate 1000 random numbers

# Histogram
plt.hist(data, bins=30, color='blue', edgecolor='black')

# Labels and title
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram Example")

# Show the plot
plt.show()

##############################################################
##############################################################
# PIE CHART
##############################################################
##############################################################
labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [40, 25, 20, 15]
colors = ['blue', 'red', 'green', 'orange']

# Create Pie Chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Title
plt.title("Programming Language Popularity")

# Show plot
plt.show()

######################################################################
######################################################################
# SUB PLOT
######################################################################
######################################################################
# Creating subplots (2 rows, 2 columns)
plt.figure(figsize=(10, 6))

# First subplot
plt.subplot(2, 2, 1)
plt.plot(x, y, 'r--')
plt.title("Line Plot")

# Second subplot
plt.subplot(2, 2, 2)
plt.bar(categories, values, color='g')
plt.title("Bar Chart")

# Third subplot
plt.subplot(2, 2, 3)
plt.hist(data, bins=20, color='b')
plt.title("Histogram")

# Fourth subplot
plt.subplot(2, 2, 4)
plt.scatter(x, y, color='purple')
plt.title("Scatter Plot")

# Adjust layout and show plot
plt.tight_layout()
plt.show()

#################################################################
#################################################################
# SAVING A PLOT
#################################################################
#################################################################
plt.plot(x, y, color='red')
plt.title("Saving a Plot")

# Save as PNG file
plt.savefig("plot.png", dpi=300)

# Show plot
plt.show()


###########################################################
###########################################################
# ADVANCED CUSTOMIZATION
###########################################################
###########################################################
# changing figure size
plt.figure(figsize=(8, 5))  # Set figure size
plt.plot(x, y, color='blue')
plt.show()

# Adding legends
plt.plot(x, y, label="Line 1", color='red')
plt.plot(x, [i*1.5 for i in y], label="Line 2", color='green')

plt.legend()  # Display legend
plt.show()
