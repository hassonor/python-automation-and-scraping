import praw
from decouple import config  # Create .env file and put there all the vars. Then call it with config.


def create_new_post_reddit(subreddit):
    reddit = praw.Reddit(user_agent=True, client_id=config('REDDIT_CLIENT_ID'),
                         client_secret=config('REDDIT_CLIENT_SECRET'),
                         username=config('REDDIT_USERNAME'),
                         password=config('REDDIT_PASSWORD'))

    subreddit = reddit.subreddit(subreddit)
    subreddit.validate_on_submit = True

    title = 'Hey From Or Hasson :-), This is my new Python Bot'
    content = """
    Hey, I am just trying out Python!
    This is my first post! :-)
    Cheers!
    Or Hasson
    """

    subreddit.submit(title=title, selftext=content)


create_new_post_reddit("pythonsandlot")  # 'pythonsandlot' used to create post with bot
