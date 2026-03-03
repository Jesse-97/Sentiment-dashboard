import streamlit as st
import pandas as pd
from src.sentiment import get_vader_sentiment
from src.cleaner import clean_text
from src.charts import *

st.set_page_config(
    page_title='Sentiment Dashboard',
    layout='wide'
)

st.title('Social Media Sentiment Dashboard')
st.markdown('Analyze public sentiment on any topic in real time.')

# Sidebar Config

with st.sidebar:
    st.header('Settings')
    topic = st.text_input('Topic / Keyword', value='IPL 2025')
    source = st.selectbox('Data Source', ['Pre-loaded CSV', 'Scrape live'])
    sentiment_filter = st.multiselect(
        'Filter by sentiment',
        ['Positive', 'Negative', 'Neutral'],
        default=['Positive', 'Negative', 'Neutral']
    )

# Loading Data

df = pd.read_csv('data/processed_tweets.csv')
df = df[df['sentiment'].isin(sentiment_filter)]

# Metrics 

col1, col2, col3, col4 = st.columns(4)
col1.metric('Total Posts',    len(df))
col2.metric('Positive',       len(df[df.sentiment=='Positive']))
col3.metric('Negative',       len(df[df.sentiment=='Negative']))
col4.metric('Avg Score',      round(df['vader_score'].mean(), 3))

# Charts

col_a, col_b = st.columns(2)
with col_a:
    st.plotly_chart(plot_sentiment_pie(df), use_container_width=True)
with col_b:
    st.plotly_chart(plot_sentiment_timeline(df), use_container_width=True)

st.plotly_chart(plot_score_distribution(df), use_container_width=True)

## Word Clouds

col_c, col_d = st.columns(2)
with col_c:
    st.subheader('Most Common Words : Positive Posts')
    st.pyplot(plot_wordcloud(df, 'Positive'))
with col_d:
    st.subheader('Most Common Words : Negative Posts')
    st.pyplot(plot_wordcloud(df, 'Negative'))

st.subheader('Top 10 Posts by Sentiment Score')
st.dataframe(
    df.nlargest(10, 'vader_score')[['text','vader_score','sentiment']],
    use_container_width=True
)
