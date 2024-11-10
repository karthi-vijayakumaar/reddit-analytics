import praw
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_reddit_posts():
    # Initialize Reddit client
    reddit = praw.Reddit(
        client_id=os.getenv('REDDIT_CLIENT_ID'),
        client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
        user_agent=os.getenv('REDDIT_USER_AGENT')
    )

    # Fetch posts from a specific subreddit
    subreddit = reddit.subreddit('datascience')
    posts = []
    
    for post in subreddit.hot(limit=100):
        posts.append({
            'title': post.title,
            'score': post.score,
            'num_comments': post.num_comments,
            'created_utc': pd.to_datetime(post.created_utc, unit='s'),
            'upvote_ratio': post.upvote_ratio,
            'author': str(post.author),
            'url': post.url
        })
    
    df = pd.DataFrame(posts)
    df.to_csv('./data/raw_reddit_data.csv', index=False)
    return 'Data fetched successfully'

if __name__ == '__main__':
    print(fetch_reddit_posts())
