# 📊 Social Media Sentiment Dashboard (Whatson)

**Live Demo:** [click here](https://whatson.streamlit.app/)

## What it does
Analyzes public sentiment on any topic using real Twitter data.
Built an end-to-end pipeline: scraping → cleaning → VADER sentiment
analysis → interactive Streamlit dashboard.

## Key Features
- Scrapes 1000+ posts on any keyword in seconds
- Dual model analysis: VADER + TextBlob comparison
- Interactive charts: sentiment breakdown, timeline, score distribution
- Word clouds for positive vs negative posts
- Top posts ranked by sentiment score

## Tech Stack
Python | snscrape | VADER | Pandas | Plotly | Streamlit

## Results
Analyzed 1,200 tweets about 'IPL 2025'. Found 58% positive sentiment,
peaking during match days. VADER vs TextBlob agreement rate: 84%.

## Limitations & Future Work
- VADER struggles with Hinglish and sarcasm
- Would improve with a fine-tuned multilingual model

## How to run locally
pip install -r requirements.txt
streamlit run app.py