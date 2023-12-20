# Reddit Posts Analysis

This repository contains an implementation to demonstrate how to scrape subreddit posts, generate metrics, and do plotting to understand the productivity of contributors.
For a particular analysis, I scrapped the top posts from two subreddits, [r/reactjs](https://www.reddit.com/r/reactjs/) and [r/node](https://www.reddit.com/r/node/), given the period 01/2023-03/2023.


## Environment Setup
- Install Python
- Check if you can access `pip` and `git` from your terminal. 
- Clone the repository https://github.com/tamal3472/Reddit-Posts-Analysis.git.
- Install the following packages-

     ```bash
       pip install praw pandas textblob matplotlib seaborn
     ```

## Getting Started

- To scrap data from [Reddit](https://www.reddit.com/), we need to create an application from Reddit from this link https://www.reddit.com/prefs/apps.
Fill up the fields like the following to get the id, secret, and user agent(name of the application-
![image](https://github.com/tamal3472/Reddit-Posts-Analysis/assets/44064679/793c7c5b-1095-437e-b3e6-e720a2ab1c12)

- Replace the '*****' with your credentials in the file [scrape_and_save_subreddit_metrics.py](https://github.com/tamal3472/Reddit-Posts-Analysis/blob/main/scrape_and_save_subreddit_metrics.py)
  ```bash
       # Replace with your Reddit API credentials
       CLIENT_ID = '************'
       CLIENT_SECRET = '**********'
       USER_AGENT = '************'
     ```
- Run the [scrape_and_save_subreddit_metrics.py](https://github.com/tamal3472/Reddit-Posts-Analysis/blob/main/scrape_and_save_subreddit_metrics.py) file to generate the CSVs with one unique identifier(post_id), 5 metrics(___post_length___, ___score___, ___total_reactions___, ___num_comments___, ___sentiment___), and created date. So that you know – the generated CSV naming will be based on the subreddit name you provide. Additionally, you can modify the time range by changing the variables inside the file.

- Run the [plotting_over_metrics.py](https://github.com/tamal3472/Reddit-Posts-Analysis/blob/main/plotting_over_metrics.py) file to see the plottings of the generated metrics data.

- Run the [per_day_post_count_plotting.py](https://github.com/tamal3472/Reddit-Posts-Analysis/blob/main/per_day_post_count_plotting.py) file to see the per day post count over the period.

## Limitations of this Scrapping Mechanism

Currently, Reddit does not [support the time-range filtering](https://www.reddit.com/r/redditdev/comments/fxfslf/how_to_scrape_data_from_a_time_period/), and no more than [1000 submissions can be extracted with their API](https://www.reddit.com/r/redditdev/comments/14zhhsb/is_there_a_way_to_scrape_more_recent_reddit_data/). An alternative solution can be [pushshift](https://github.com/pushshift/api), but this is 3rd party separate storage system and recently added [their authorization system with special permission with your Reddit account](https://api.pushshift.io/signup). 

Due to this demo project purpose, I used the Reddit API using Praw acknowledging the data limitation.


## Selection of Metrics

I selected the following 5 important metrics ___post_length___, ___score___, ___total_reactions___, ___num_comments___, and ___sentiment___ for the analysis of the productivity of contributors between two subreddits.

- ___post_length___: Post length is important to understand engagement and interest level. For example - Longer posts may indicate that users are willing to invest more time in creating and consuming content. On the contrary,
Shorter posts might suggest that the community prefers quick and concise communication.

- ___score___: The score of the subreddit submission is the best way to do the Quality Assessment of the submission. Community feedback is required to understand the contributor's quality.

- ___total_reactions___: This metric provides valuable information about community engagement over the submissions.
  
- ___num_comments___: This provides the depth of discussion for the post topic and proofs the users' participation.

- ___sentiment___: Doing the sentiment polarity analysis of the posts can help to understand the reputation, community dynamics, and content effectiveness.


## Understanding the Differences in Distribution of the Metrics across Two Sub-reddits
After histogram plotting the data of sub-reddits the graphical layout of the metrics-

![image](https://github.com/tamal3472/Reddit-Posts-Analysis/assets/44064679/ec2fad9e-e60e-4a27-80cd-59f5997f0379)

**It is evident from the figure that ReactJS submissions received more social interactions and community engagement than the NodeJS community, even though the two groups subreddit posts had similar lengths and sentiments.**

This outcome also validates the notion that a larger subreddit attracts more user engagement than a smaller one, as ReactJS has 123k<sup>*</sup> more members than the NodeJS Community.

*_As of December 20, 2023, the ReactJS community had 373,000 members, while the NodeJS community had 250,000 members._


## Additional Type of Analysis
To better visualize the post activity over time in two subreddits, I did an additional analysis by considering the number of daily posts submitted between January and March 2023. While generating the metrics, we also added the creation date(___created_date___) of each post in the CSV file. Now, this allows us to create a daily count plot of the posts over the given period, providing valuable insights into the posting trends.

The plotted graph looks like this - 

![image](https://github.com/tamal3472/Reddit-Posts-Analysis/assets/44064679/23d37050-327b-4fb3-adae-8b13839929d3)

**From the figure, it is apparent that overall the ReacJS group posted more submissions per day than the NodeJS community. However, there are some spikes in March 2023.**

I searched for any NodeJS version releases or issues on March 2023 to understand the reason for the outliers. I found that, in March, there was an [infrastructure incident](https://nodejs.org/en/blog/announcements/node-js-march-17-incident) and developers could not download Node.JS for almost 2 days, also they released [a new version](https://docs.snowflake.com/en/release-notes/clients-drivers/nodejs-2023#version-1-6-20-march-23-2023) with some fixes in March. I am assuming the spikes happened for that reason. However, we can validate this assumption by looking at the post details and I left that for future work.

