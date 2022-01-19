import praw
from decouple import config  # Create .env file and put there all the vars. Then call it with config.
from datetime import datetime, timedelta


def get_all_posts_24h_by_subject_on_reddit(subreddit):
    reddit = praw.Reddit(user_agent=True, client_id=config('REDDIT_CLIENT_ID'),
                         client_secret=config('REDDIT_CLIENT_SECRET'),
                         username=config('REDDIT_USERNAME'),
                         password=config('REDDIT_PASSWORD'))
    subreddit = reddit.subreddit(subreddit)
    posts24h = []
    with open('output_last_24h_posts.txt', 'w') as file:
        for post in subreddit.new():
            current_time = datetime.utcnow()  # getting the current time (utc local time)
            post_time = datetime.utcfromtimestamp(post.created)  # convert timestamp to utc format

            delta_time = current_time - post_time  # find the delta between current time to post created time
            # print(delta_time)
            if delta_time <= timedelta(hours=24):  # create timedelta object (same object like delta_time)
                posts24h.append((post.title, post.selftext, post_time))
                file.write(f'{post.title}\n{post.selftext}\n\n')
            print(posts24h)


get_all_posts_24h_by_subject_on_reddit("selenium")
