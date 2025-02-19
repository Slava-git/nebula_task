import pandas as pd


def calculate_metrics(df: pd.DataFrame) -> dict:

    mean_rating = df['rating'].mean()
    rating_percentages = (df['rating']
                          .value_counts(normalize=True)
                          .mul(100)
                          .to_dict())
    na_counts = df.isna().sum().to_dict()
    
    return {
        "mean_rating": mean_rating,
        "rating_percentages": rating_percentages,
        "na_counts": na_counts
    }