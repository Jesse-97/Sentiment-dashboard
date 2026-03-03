import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

def plot_sentiment_pie(df):
    counts = df['sentiment'].value_counts().reset_index()
    counts.columns = ['Sentiment', 'Count']
    fig = px.pie(
        counts, values='Count', names='Sentiment',
        color='Sentiment',
        color_discrete_map={
            'Positive': '#2ECC71',
            'Negative': '#E74C3C',
            'Neutral': '#95A5A6',
        },
        hole=0.4,
        title='Overall Sentiment Distribution'
    )
    return fig

def plot_sentiment_timeline(df):
    df['date'] = pd.to_datetime(df['date']).dt.date
    daily = df.groupby(['date','sentiment']).size().reset_index(name='count')
    fig = px.line(
        daily, x='date', y='count', color='sentiment',
        color_discrete_map={
            'Positive': '#2ECC71',
            'Negative': '#E74C3C',
            'Neutral':  '#95A5A6'
        },
        title='Sentiment Trends Over Time'
    )
    return fig

def plot_wordcloud(df, sentiment_filter=None):
    if sentiment_filter:
        text = ' '.join(df[df['sentiment'] == sentiment_filter]['clean_text'])
    else:
        text = ' '.join(df['clean_text'])
    
    wc = WorldCloud(
        widht=800, height=400,
        background_color='white',
        colormap='Blues' if sentiment_filter =='Positive' else 'Reds'
    ).generate(text)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wc, interpolation='bilinear')
    ax.axis('off')
    return fig

def plot_score_distribution(df):
    fig = px.histogram(
        dfm, x='vader_score', nbins=30,
        title='Distribution of Sentiment Score',
        color_discrete_sequence=['#3498DB']
    )
    fig.add_vline(x=0.05, line_dash='dash', line_color='green')
    fig.add_vline(x=-0.05, line_dash='dash', line_color='red')
    return fig


     