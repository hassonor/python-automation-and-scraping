import nltk

nltk.download('vader_lexicon')
nltk.download('twitter_samples')
from nltk.sentiment import SentimentIntensityAnalyzer


def get_positive_score_tweets(tweets_database):
    positive_random_tweets = []
    for tweet in tweets_database:
        if analyzer.polarity_scores(tweet)['compound'] > 0:
            positive_random_tweets.append(tweet)

    return positive_random_tweets


analyzer = SentimentIntensityAnalyzer()
text1 = "Hey, what a beautiful day! How amazing it is!"
text2 = "Hey, I hate  covid-19!"

print(analyzer.polarity_scores(text1)['compound'])  # score -> 0.8513 (positive text)
print(analyzer.polarity_scores(text2)['compound'])  # score -> -0.6114 (negative text)

random_tweets = nltk.corpus.twitter_samples.strings()  # get 30,000 random tweets
print("Total tweets on database: " + str(len(random_tweets)))  # total tweets
print("Total positive text tweets: " + str(len(get_positive_score_tweets(random_tweets))))  # total positive tweets
