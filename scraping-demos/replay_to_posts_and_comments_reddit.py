from datetime import timedelta, datetime

import praw
from decouple import config  # Create .env file and put there all the vars. Then call it with config.


def create_new_post_reddit(subreddit):
    reddit = praw.Reddit(user_agent=True, client_id=config('REDDIT_CLIENT_ID'),
                         client_secret=config('REDDIT_CLIENT_SECRET'),
                         username=config('REDDIT_USERNAME'),
                         password=config('REDDIT_PASSWORD'))

    subreddit = reddit.subreddit(subreddit)

    for post in subreddit.new():
        current_time = datetime.utcnow()
        post_time = datetime.utcfromtimestamp(post.created)
        delta_time = current_time - post_time
        if delta_time <= timedelta(hours=48):
            if "Or Hasson" in post.title:  # Comment to post contain title with "Or Hasson" :)
                print(post.title)
                post.reply('Hey, Or Hasson :-)! Welcome to Reddit!')
                for comment in post.comments:  # comment to comment contain "Welcome to Reddit!" :)
                    if "Welcome to Reddit!" in comment.body:
                        comment.reply("Yeah, it's coming")


create_new_post_reddit("pythonsandlot")
