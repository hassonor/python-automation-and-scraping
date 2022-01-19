import praw
from decouple import config  # Create .env file and put there all the vars. Then call it with config.

reddit = praw.Reddit(user_agent=True, client_id=config('REDDIT_CLIENT_ID'),
                     client_secret=config('REDDIT_CLIENT_SECRET'),
                     username=config('REDDIT_USERNAME'),
                     password=config('REDDIT_PASSWORD'))

url = config("REDDIT_POST_TO_SCRAPING")

post = reddit.submission(url=url)

# print(post.title)
# print(post.selftext) # Get the body of the post

# Get the comments of the post
print(len(post.comments))  # Get the number of comments for the post
for comment in post.comments:
    print(comment.body)
