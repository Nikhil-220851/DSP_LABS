# Import the required Python libraries (pandas, numpy, matplotlib, seaborn).
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset into a pandas DataFrame
data = pd.read_csv("Customer Purchasing Behaviors.csv")
# Display the number of rows and columns in the dataset
print("No of rows and columns: ", data.shape)
# Print the column names of the dataset
print("Name of the columns: ",data.columns)
# Display the first 5 rows of the dataset
print("First 5 rows of the dataset: ")
print(data.head())
# Check the data type of each column
print("the datatype of each column: ")
print(data.dtypes)
# Identify the number of missing values in each column
print("the missing values of each column: ")
print(data.isnull().sum())

numerical_col = data.select_dtypes(include=np.number).columns
categorical_col = data.select_dtypes(include=['object', 'string']).columns
# Fill missing values in numerical columns using the mean
data[numerical_col] = data[numerical_col].fillna(data[numerical_col].mean())
# Fill missing values in categorical columns using the mode
data[categorical_col] = data[categorical_col].fillna(data[categorical_col].mode().iloc[0])
# Verify that there are no missing values remaining
print("the missing values of each column after handling: ")
print(data.isnull().sum())
# Calculate the mean for all numerical columns
print("The mean of numerical columns: ")
print(data[numerical_col].mean())
# Calculate the median for all numerical columns
print("The median of numerical columns: ")
print(data[numerical_col].median())
# Calculate the standard deviation for all numerical columns
print("The standard deviation of numerical columns: ")
print(data[numerical_col].std())
# Find the minimum and maximum values for numerical columns
print("The max and min of numerical columns: ")
print(data[numerical_col].agg([max, min]))
# Generate a summary using describe()
print("The summary using describe(): ")
print(data.describe())
# Create a histogram for the purchase amount column
plt.hist(data['purchase_amount'], bins=20)
plt.title('Distribution of Purchase Amount')
plt.xlabel('Purchase Amount')
plt.ylabel('Frequency')
plt.show()
# Create a bar chart showing the count of customers by purchase_amount
sns.countplot(x=data['purchase_amount'])
plt.title('Count of Customers by Purchase Amount')
plt.xlabel('Purchase Amount')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()
# Create a box plot for the purchase amount column
sns.boxplot(x=data['purchase_amount'])
plt.title('Boxplot of Purchase Amount')
plt.xlabel('Purchase Amount')
plt.xticks(rotation=45)
plt.show()
# Create a scatter plot between age and purchase amount
sns.scatterplot(x=data['age'],y=data['purchase_amount'])
plt.title('Scatter Plot of Age vs Purchase Amount')
plt.xlabel('Age')
plt.ylabel('Purchase Amount')
plt.show()
# Display a correlation heatmap for numerical columns.
plt.figure(figsize=(10, 8))
sns.heatmap(data[numerical_col].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()