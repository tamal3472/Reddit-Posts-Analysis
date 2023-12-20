import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file into a DataFrame
file_path = "reactjs_metrics.csv"  # Replace with the actual path to your CSV file
df_subreddit1 = pd.read_csv(file_path)
file_path = "node_metrics.csv"  # Replace with the actual path to your CSV file
df_subreddit2 = pd.read_csv(file_path)

subreddit1 = 'ReactJS'
subreddit2 = 'NodeJS'


# Plotting
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15, 10))
fig.suptitle(f"Distribution of Metrics in {subreddit1} and {subreddit2}")

# Post Length
sns.histplot(df_subreddit1["post_length"], kde=True, ax=axes[0, 0], label=subreddit1)
sns.histplot(df_subreddit2["post_length"], kde=True, ax=axes[0, 0], label=subreddit2)
axes[0, 0].set_title("Post Length Distribution")
axes[0, 0].legend()

# Score
sns.histplot(df_subreddit1["score"], kde=True, ax=axes[0, 1], label=subreddit1)
sns.histplot(df_subreddit2["score"], kde=True, ax=axes[0, 1], label=subreddit2)
axes[0, 1].set_title("Score Distribution")
axes[0, 1].legend()

# Total Reactions Count
sns.histplot(df_subreddit1["total_reactions"], kde=True, ax=axes[0, 2], label=subreddit1)
sns.histplot(df_subreddit2["total_reactions"], kde=True, ax=axes[0, 2], label=subreddit2)
axes[0, 2].set_title("Total Reactions Count Distribution")
axes[0, 2].legend()

# Number of Comments
sns.histplot(df_subreddit1["num_comments"], kde=True, ax=axes[1, 0], label=subreddit1)
sns.histplot(df_subreddit2["num_comments"], kde=True, ax=axes[1, 0], label=subreddit2)
axes[1, 0].set_title("Number of Comments Distribution")
axes[1, 0].legend()

# Sentiment
sns.histplot(df_subreddit1["sentiment"], kde=True, ax=axes[1, 1], label=subreddit1)
sns.histplot(df_subreddit2["sentiment"], kde=True, ax=axes[1, 1], label=subreddit2)
axes[1, 1].set_title("Sentiment Distribution")
axes[1, 1].legend()

# Hide the empty subplot
axes[1, 2].axis("off")

plt.show()
