import pandas as pd
from transformers import pipeline


sentiment_pipeline = pipeline(
    "text-classification", 
    model="lxyuan/distilbert-base-multilingual-cased-sentiments-student"
)


def add_sentiment(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['sentiment'] = df['review_text'].apply(
        lambda text: sentiment_pipeline(text)[0]['label']
    )
    return df