# =========================================
# Movie Rating Classification Project
# =========================================

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# =========================================
# Step 1: Load Dataset
# =========================================

data = pd.read_csv("IMDB-Movie-Data.csv")

print("First 5 rows of dataset:")
print(data.head())

print("\nDataset shape:", data.shape)

print("\nInitial missing values:")
print(data.isnull().sum())

# =========================================
# Step 2: Data Cleaning
# =========================================

# Drop irrelevant text columns
data.drop(
    columns=['Title', 'Description', 'Director', 'Actors'],
    inplace=True
)

# Fill missing numerical values with mean
data['Revenue (Millions)'].fillna(
    data['Revenue (Millions)'].mean(),
    inplace=True
)

data['Metascore'].fillna(
    data['Metascore'].mean(),
    inplace=True
)

print("\nMissing values after cleaning:")
print(data.isnull().sum())

# =========================================
# Step 3: Create Target Label
# =========================================

# High Rated (1) if Rating >= 7 else Low Rated (0)
data['label'] = (data['Rating'] >= 7).astype(int)

print("\nLabel distribution:")
print(data['label'].value_counts())

# =========================================
# Step 4: Feature Engineering
# =========================================

# One-hot encode Genre column
genre_encoded = data['Genre'].str.get_dummies(sep=',')

# Combine genre features with main dataset
data = pd.concat([data, genre_encoded], axis=1)

# Drop original Genre column
data.drop('Genre', axis=1, inplace=True)

# Define features and target
features = data.drop(['Rating', 'label', 'Rank', 'Year'], axis=1)
target = data['label']

# 🔑 VERY IMPORTANT: remove any remaining NaN values
features = features.fillna(0)

print("\nFeature matrix shape:", features.shape)

# =========================================
# Step 5: Exploratory Data Analysis (EDA)
# =========================================

# Rating vs Votes
plt.scatter(data['Votes'], data['Rating'])
plt.xlabel("Votes")
plt.ylabel("Rating")
plt.title("Rating vs Votes")
plt.show()

# Rating vs Revenue
plt.scatter(data['Revenue (Millions)'], data['Rating'])
plt.xlabel("Revenue (Millions)")
plt.ylabel("Rating")
plt.title("Rating vs Revenue")
plt.show()

# Rating vs Runtime
plt.scatter(data['Runtime (Minutes)'], data['Rating'])
plt.xlabel("Runtime (Minutes)")
plt.ylabel("Rating")
plt.title("Rating vs Runtime")
plt.show()

# =========================================
# Step 6: Train-Test Split
# =========================================

X_train, X_test, y_train, y_test = train_test_split(
    features,
    target,
    test_size=0.2,
    random_state=42
)

print("\nTraining data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)

# =========================================
# Step 7: Train Logistic Regression Model
# =========================================

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

print("\nModel training completed successfully.")

# =========================================
# Step 8: Model Evaluation
# =========================================

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# =========================================
# Project Complete
# =========================================

print("\nMovie Rating Classification Project executed successfully!")
