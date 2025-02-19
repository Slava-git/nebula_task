## Approach

This project is built using FastAPI. 
I isolated business logic—such as metrics calculation, sentiment analysis, and keyword extraction into individual modules. 

## Report
Navigate to ```report.txt```

## Video demo
[Watch the Video Demo](https://www.loom.com/share/3f357e8dd6c34ce8b9c37556c6dcb8b4?sid=b885102f-576a-49fa-864a-01475136ce43)


## Requirements

- Python 3.10
- ```pip install -r requirements.txt```
- sign up in https://dataforseo.com/ to get email, password, review id. Put these values into environment variables: RESTCLIENT_EMAIL, RESTCLIENT_PASSWORD, REVIEW_ID.

## Run the API
- ```cd src```
- ```uvicorn src.main:app --reload```


## API Usage

Below are a few examples of how you can interact with the API using `curl`.

#### Get Raw Reviews
Retrieve the complete, unprocessed review data from the external API.

```bash
curl -X GET http://localhost:8000/raw_reviews
```

#### Get Processed Reviews
Fetch review data with essential fields (rating, id, title, and review_text) extracted

```bash
curl -X GET http://localhost:8000/reviews
```

#### Calculate Metrics
Submit a list of reviews to calculate metrics such as average rating, rating distribution, and missing values count.

```bash
curl -X POST -H "Content-Type: application/json" -d '[
  {
    "rating": 5,
    "id": "review123",
    "title": "Amazing App",
    "review_text": "I love using this app every day!"
  },
  {
    "rating": 2,
    "id": "review456",
    "title": "Needs Improvement",
    "review_text": "The app crashes frequently and has many bugs."
  }
]' http://localhost:8000/metrics
```

#### Get Sentiment
Perform sentiment analysis on the provided reviews.

```bash
curl -X POST -H "Content-Type: application/json" -d '[
  {
    "rating": 5,
    "id": "review123",
    "title": "Amazing App",
    "review_text": "I love using this app every day!"
  },
  {
    "rating": 2,
    "id": "review456",
    "title": "Needs Improvement",
    "review_text": "The app crashes frequently and has many bugs."
  }
]' http://localhost:8000/sentiment
```

#### Extract Keywords
Extract the top N keywords from negative reviews. 

```bash
curl -X POST -H "Content-Type: application/json" -d '[
  {
    "rating": 1,
    "id": "review789",
    "title": "Terrible Experience",
    "review_text": "This is the worst app I've ever used. It crashes all the time!"
  },
  {
    "rating": 2,
    "id": "review456",
    "title": "Needs Improvement",
    "review_text": "The app crashes frequently and has many bugs."
  }
]' "http://localhost:8000/keywords?n=10"
```
