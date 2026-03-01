import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
import nltk
nltk.download('vader_lexicon', quiet=True)

sia = SentimentIntensityAnalyzer()

def get_vader_sentiment(text):
    scores = sia.polarity_scores(text)
    compound = scores['compound']

    if compound >= 0.05:
        label = 'Positive'
    elif compound <= -0.05:
        label = 'Negative'
    else:
        label = 'Neutral'
    return compound, label

def get_textblob_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    if polarity > 0.05:
        label = 'Positive'
    elif polarity < -0.05:
        label = 'Negative'
    else: 
        label = 'Neutral'
    
    return polarity, subjectivity, label

def score_dataframe(csv_path):
   df = pd.read_csv(csv_path)
   print("Scoring with VADER...")
   df[['vader_score', 'vader_label']] = df['clean_text'].apply(
       lambda x: pd.Series(get_vader_sentiment(x))
   )
   print("Scoring with TextBlob...")
   df[['tb_polarity', 'tb_subjectivity', 'tb_label']] = df['clean_text'].apply(
       lambda x: pd.Series(get_textblob_sentiment(x))
   )
   df.to_csv(csv_path, index=False)
   print(f"Done! Scored {len(df)} rows.")
   print("\nVADER sentiment breakdown:")
   print(df['vader_label'].value_counts())
   print("\nTextBlob sentiment breakdown:")
   print(df['tb_label'].value_counts())
   return df
        
if __name__ == '__main__':
    score_dataframe('data/processed_tweets.csv')