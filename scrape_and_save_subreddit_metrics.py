import praw
import pandas as pd
from textblob import TextBlob
from datetime import datetime

SUBREDDIT_REACTJS = 'reactjs'
SUBREDDIT_NODE = 'node'
SCRAPE_START_DATE = datetime(2023, 1, 1)
SCRAPE_END_DATE = datetime(2023, 3, 31)
YEAR_TIME_FILTER = 'year'


# Replace with your Reddit API credentials
CLIENT_ID = '************'
CLIENT_SECRET = '**********'
USER_AGENT = '************'

reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT
)


# This method prepares the metrics per post.
def prepare_metrics_per_post(post):
    post_id = post.id
    post_length = len(post.selftext.split())
    score = post.score
    total_reactions = post.downs + post.ups  # The count  of People interaction on a particular post
    num_comments = post.num_comments
    post_text = post.title + " " + post.selftext
    sentiment = TextBlob(post_text).sentiment.polarity  # To get the sentimental polarity of each post

    # post id as a unique identifier
    # 5 metrics and created_date for additional analysis
    return {
        "post_id": post_id,
        "post_length": post_length,
        "score": score,
        "total_reactions": total_reactions,
        "num_comments": num_comments,
        "sentiment": sentiment,
        "created_date": datetime.utcfromtimestamp(post.created_utc).strftime('%Y-%m-%d'),
    }


# This method scrapes the subreddit and filters by given time range
def scrape_reddit_posts(subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    scrapped_posts = []

    # Currently, Reddit does not support time range filters.
    # So we are scraping the top posts of a year and filtering them manually by the given time range
    for post in subreddit.top(time_filter=YEAR_TIME_FILTER, limit=None):
        post_time = datetime.utcfromtimestamp(post.created_utc)
        if SCRAPE_START_DATE <= post_time <= SCRAPE_END_DATE:
            scrapped_posts.append(prepare_metrics_per_post(post))

    return scrapped_posts


# This method is generating and saving the metrics into a CSV
def generate_and_write_to_csv(subreddit_name):
    posts_data = scrape_reddit_posts(subreddit_name)
    df = pd.DataFrame(posts_data)
    df.to_csv(f"{subreddit_name}_metrics.csv", index=False)


if __name__ == "__main__":
    generate_and_write_to_csv(SUBREDDIT_REACTJS)
    generate_and_write_to_csv(SUBREDDIT_NODE)
