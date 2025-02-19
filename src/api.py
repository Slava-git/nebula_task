import pandas as pd
import os
from dotenv import load_dotenv
from typing import List

from fastapi import FastAPI, HTTPException

from clients.client import RestClient
from logic.statistics import calculate_metrics
from logic.sentiment import add_sentiment
from logic.keywords import get_top_keywords
from schemas import Review

load_dotenv()

restclient_email = os.getenv("RESTCLIENT_EMAIL")
restclient_password = os.getenv("RESTCLIENT_PASSWORD")
review_id = os.getenv("REVIEW_ID")

app = FastAPI()

client = RestClient(restclient_email, restclient_password)


@app.get("/raw_reviews")
async def get_raw_reviews():
    response = client.get(f"/v3/app_data/google/app_reviews/task_get/advanced/{review_id}")

    if response.get("status_code") != 20000:
        raise HTTPException(status_code=400, detail="Failed to get reviews")
    
    return response

@app.get("/reviews")
async def get_reviews():
    
    response = client.get(f"/v3/app_data/google/app_reviews/task_get/advanced/{review_id}")

    
    if response.get("status_code") != 20000:
        raise HTTPException(status_code=400, detail="Failed to get reviews")
    
    try:
        items = response['tasks'][0]['result'][0]['items']
    except (KeyError, IndexError) as e:
        raise HTTPException(status_code=500, detail="Unexpected response format") from e


    data = {
        'rating': [item['rating']['value'] for item in items],
        'id': [item['id'] for item in items],
        'title': [item['title'] for item in items],
        'review_text': [item['review_text'] for item in items]
    }
    
    return data


@app.post("/metrics")
async def get_metrics(data: List[Review]):
    df = pd.DataFrame([review.dict() for review in data])
    
    metrics = calculate_metrics(df)
    return metrics


@app.post("/sentiment")
async def get_sentiment(data: List[Review]):
    df = pd.DataFrame([review.dict() for review in data])
    
    df_with_sentiment = add_sentiment(df)
    return df_with_sentiment.to_dict(orient="records")


@app.post("/keywords")
async def get_keywords(data: List[Review], n: int = 20):

    df = pd.DataFrame([review.dict() for review in data])
    
    df_with_sentiment = add_sentiment(df)
    
    try:
        common_keywords = get_top_keywords(df_with_sentiment, n)
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return {"top_keywords": common_keywords}