import re
import pandas as pd

def clean_text(text):
    if not isinstance(text, str):
        return ''
    text = re.sub(r'http\S+', '', text) #removing URLS
    text = re.sub(r'@\w+', '', text) #remove @mentions
    text = re.sub(r'#(\w+)', r'\1', text) #remove # but keep words
    text = re.sub(r'RT\s*:', '', text) # remove retweet tag
    text = re.sub(r'[^\w\s!?.,]', '', text) # remove special chars
    text = re.sub(r'\s+', ' ', text).strip() # collapse whitespace
    return text.lower()

def process_dataframe(csv_path):
    df = pd.read_csv(csv_path, encoding='latin-1', header=None)
    df.columns = ['sentiment', 'id', 'date', 'query', 'username', 'text']
    df['sentiment'] = df['sentiment'].map({0: 'Negative', 4: 'Positive'})
    df = df.sample(n=10000, random_state=42).reset_index(drop=True)
    df = df.dropna(subset=['text'])
    df = df.drop_duplicates(subset=['text'])
    df['clean_text'] = df['text'].apply(clean_text)
    df = df[df['clean_text'].str.len() > 10]
    df.to_csv('data/processed_tweets.csv', index=False)
    print(f'Clean data: {len(df)} rows saved to data/processed_tweets.csv')
    return df

if __name__ == '__main__':
    process_dataframe('data/raw_tweets.csv')