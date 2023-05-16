import praw
import sympy
import praw_credentials
import time

# Reddit API credentials
client_id = praw_credentials.client_id
client_secret = praw_credentials.client_secret
username = praw_credentials.username
password = praw_credentials.password
user_agent = praw_credentials.user_agent

# Initialize the Reddit instance
reddit = praw.Reddit(
 client_id=client_id,
 client_secret=client_secret,
 username=username,
 password=password,
 user_agent=user_agent
)

# Subreddit to monitor
subreddit = reddit.subreddit("math")


# Stream all new comments in the subreddit
for comment in subreddit.stream.comments(skip_existing=True):
    time.sleep(3)
    print(comment.author.link_karma)
    # Check if the comment author has prime karma above 100
    if sympy.isprime(comment.author.link_karma) and comment.author.link_karma > 100:
        reply_message = f"You have {comment.author.link_karma} post karma, which is a prime number!"
        comment.reply(reply_message)
        print("we have a hit")
        
