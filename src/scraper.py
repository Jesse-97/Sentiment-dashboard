import snscrape.modules.twitter as sntwitter
import pandas as pandas

def scrape_tweets(keywords, max_results=1000):
    tweets = []
    query = f'{keyword} lang:en since:2025-01-01'

    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        if len(tweets) >= max_results:
            break
        tweets.append({
            'date' : tweet.date,
            'username' : tweet.user.username,
            'text' : tweet.rawContent,
            'likes' : tweet.likeCount,
            'retweets' : tweet.retweetCount,
        })
    
    df = pd.DatatFrame(tweets)
    df.to_csv('data/raw_tweets.csv', index=False)
    print(f'Scraped {len(df)} tweets')
    return df

if __name__ == '__main__':
    scrape_tweets('IPL 2025', max_results=1000)
