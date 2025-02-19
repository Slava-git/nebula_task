import re
from collections import Counter
import nltk

nltk.download('stopwords')
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords


lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def extract_keywords(text: str):

    words = re.findall(r'\b\w+\b', text.lower())
    words = [word for word in words if word not in stop_words]
    words = [lemmatizer.lemmatize(word) for word in words]
    return words

def get_top_keywords(df, n: int = 20):
    if 'sentiment' not in df.columns:
        raise ValueError("DataFrame must include a 'sentiment' column.")
    
    negative_reviews = df[df['sentiment'] == 'negative']['review_text']
    
    all_words = [word for review in negative_reviews for word in extract_keywords(review)]
    
    word_counts = Counter(all_words)
    
    return word_counts.most_common(n)
