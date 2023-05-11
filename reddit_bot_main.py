import praw
import sympy
import praw_credentials

# Reddit API credentials
# eplace praw_credentials with your file containing the credentials in the following format
#client_id = "YOUR_CLIENT_ID"
#client_secret = "YOUR_CLIENT_SECRET"
#username = "YOUR_REDDIT_USERNAME"
#password = "YOUR_REDDIT_PASSWORD"
#user_agent = "YOUR_USER_AGENT"

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

    # Check if the comment author has prime karma
    if sympy.isprime(comment.author.link_karma):
        if (sympy.isprime(comment.author.link_karma) > 1000):
            # Formulate the reply message

            print("We have a hit")

            ##reply_message = f"You have {comment.author.link_karma} karma, which is a prime number"

            # Reply to the comment
            ##comment.reply(reply_message)
