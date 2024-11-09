import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = '/Users/panda/Downloads/training_and_development_data.csv'
data = pd.read_csv(file_path)

# # Performing an initial Overview
# data.info()
# print(data.head())

# # Descriptive statistics for numerical columns
# print(data.describe())

# # Unique Value Analysis : trying to identify the variability within the data and potential patterns or categorical groupings
# # getting unique values for each categorical column
# unique_values = {col:data[col].unique() for col in data.select_dtypes(include=['object']).columns} 
# print(unique_values)

# # Distribution of Training Duration
# plt.figure(figsize=(12, 6))
# plt.subplot(1, 2, 1)
# sns.histplot(data['Training Duration(Days)'], bins=20, kde=True)
# plt.title('Distribution of Training Duration')
# plt.subplot(1, 2, 2)
# sns.boxplot(x=data['Training Duration(Days)'])
# plt.title('Boxplot of Training Duration')
# plt.show()

# Distribution of Training Cost
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.histplot(data['Training Cost'], bins=20, kde=True)
plt.title('Distribution of Training Cost')
plt.subplot(1, 2, 2)
sns.boxplot(x=data['Training Cost'])
plt.title('Boxplot of Training Cost')
plt.show()
