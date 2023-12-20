import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
file_path = "reactjs_metrics.csv"
df_subreddit1 = pd.read_csv(file_path)
file_path = "node_metrics.csv"
df_subreddit2 = pd.read_csv(file_path)


# Extract date from datetime
df_subreddit1['created_date'] = pd.to_datetime(df_subreddit1['created_date'])
df_subreddit2['created_date'] = pd.to_datetime(df_subreddit2['created_date'])
df_subreddit1['date'] = df_subreddit1['created_date'].dt.date
df_subreddit2['date'] = df_subreddit2['created_date'].dt.date

# Count posts per day
post_counts_1 = df_subreddit1['date'].value_counts().sort_index()
post_counts_2 = df_subreddit2['date'].value_counts().sort_index()

# Plotting
plt.figure(figsize=(14, 9))
plt.bar(post_counts_1.index, post_counts_1, width=0.4, align='center', label='ReactJS', color='skyblue')
plt.bar(post_counts_2.index, post_counts_2, width=0.4, align='edge', label='NodeJS', color='orange')
plt.xlabel('Date')
plt.ylabel('Number of Posts')
plt.title('Number of Reddit Posts Per Day for ReactJS & NodeJS from 01/2023 to 03/2024')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
