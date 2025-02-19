from pydantic import BaseModel

class Review(BaseModel):
    rating: float
    id: str
    title: str
    review_text: str