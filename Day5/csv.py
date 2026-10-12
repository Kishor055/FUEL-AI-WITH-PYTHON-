import pandas as pd

# Load the dataset
df = pd.read_csv("student_dataset_random.csv")

# Display the first five rows
print(df.head())

# Check rows and columns
print(df.shape)

# View column names
print(df.columns)

# Check missing values
print(df.isnull().sum())

# Generate statistical summaries
print(df.describe())