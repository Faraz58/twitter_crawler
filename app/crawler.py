import tweepy
from datetime import datetime

# توابع مربوط به خزش کاربران
def get_user_tweets(usernames):
    results = []
    for username in usernames:
        tweets = []
        # دریافت توییت‌های کاربر
        for tweet in api.user_timeline(screen_name=username, count=10):
            tweets.append({
                "text": tweet.text,
                "created_at": tweet.created_at,
                "like_count": tweet.favorite_count,
                "retweet_count": tweet.retweet_count,
                "type": tweet_type(tweet),
                "hashtags": [hashtag['text'] for hashtag in tweet.entities['hashtags']],
                "mentions": [mention['screen_name'] for mention in tweet.entities['user_mentions']],
                "links": [url['expanded_url'] for url in tweet.entities['urls']],
                "username": tweet.user.screen_name,
                "user_id": tweet.user.id,
                "geo": tweet.geo,
                "tweet_link": f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}"
            })
        results.append({username: tweets})
    return results

def search_by_keywords(keywords):
    # خزش بر اساس کلمات کلیدی
    results = []
    for keyword in keywords:
        tweets = []
        for tweet in api.search(q=keyword, count=10):
            tweets.append({
                "text": tweet.text,
                "created_at": tweet.created_at,
                "like_count": tweet.favorite_count,
                "retweet_count": tweet.retweet_count,
                "type": tweet_type(tweet),
                "hashtags": [hashtag['text'] for hashtag in tweet.entities['hashtags']],
                "mentions": [mention['screen_name'] for mention in tweet.entities['user_mentions']],
                "links": [url['expanded_url'] for url in tweet.entities['urls']],
                "username": tweet.user.screen_name,
                "user_id": tweet.user.id,
                "geo": tweet.geo,
                "tweet_link": f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}"
            })
        results.append({keyword: tweets})
    return results

def tweet_type(tweet):
    if tweet.in_reply_to_status_id:
        return "reply"
    elif hasattr(tweet, 'retweeted_status'):
        return "retweet"
    elif tweet.is_quote_status:
        return "quote"
    else:
        return "tweet"
