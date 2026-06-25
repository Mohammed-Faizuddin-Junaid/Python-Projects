# first part of code is to use as libraries 
# pandas help in  arranging data,loading and managing data 
import pandas as pd
# matplot lib helps us to plot graphs, visualizing data and displaying data 
import matplotlib.pyplot as plt
#pandas loads the csv file and stores it in dataframe
df= pd.read_csv("students.csv")
# For printing the table we use some codes each line of code contributing to form the table 
print("\n====Full Tablle===") 
print(df)
# Using head(1,2,3) we can see the no of rows of the table as we like , but writing only head() shows upto 5 rows by default. 
print(df.head())
# taking Average of each subject
print("\n=== Average Scores Per Subject ===")
# Using f  strings we can write what we want before or after the code for better understanding making it more logical.
print (f"Math Average:{df["Math"].mean():.1f}")
print(f"Science Average:{df["Science"].mean():.1f}")
print (f"English Average:{df["English"].mean():.1f}")
print (f"Physics Average:{df["Physics"].mean():.1f}")
#Preparing  a Bar Graph.
# List of subjects.
Subject_Names=["Math","Science","English","Physics"]

Average_Scores=[df["Math"].mean(),df["Science"].mean(),df["English"].mean(),df["Physics"].mean()]
# It gives colour to the graph. 
color=["blue","green","red","yellow"]
# using plt libraries to draw the graph
plt.bar(Subject_Names,Average_Scores,color=["blue","green","red","yellow"])
plt.title("Bar Graph showing Average Scores")
plt.xlabel("Subject_Names")
plt.ylabel("Average_Scores")
# It stores the graph in another file.
plt.savefig("Bar_Graph.png")
# It cleans the canvas for the next graph.
plt.clf()
# Now using plt libraries we are making a scatter plot. It makes points on graph which represents each student.
plt.scatter(df["Math"],df["Physics"])
plt.title("Scatter Plot of each Student")
plt.xlabel("Math")
plt.ylabel("Physics")
plt.savefig("Scatter_plot.png")
plt.clf()
# Importing seaborn and using it for creating a heatmap. ASs student 
import seaborn as sns
# this line replaces the numbers of table 0,1,2,3.. with names of the students of the table.
heatmap_data=df.set_index("Name")
sns.heatmap(heatmap_data,annot=True,cmap="Blues",fmt="d")
plt.title("HeatMap showing Students Performance")
plt.savefig("Heat_Map.png")