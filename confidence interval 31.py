import pandas as pd
import numpy as np
from scipy.stats import norm

# Create a DataFrame from the provided dataset
data = {
    'product_title': ['Pineapple slicer', 'Levis Jeans Pant', 'Wallet', 'Salwar'],
    'product_category': ['Apparel', 'Apparel', 'Apparel', 'Apparel'],
    'star_rating': [4, 5, 5, 5],
    'review_headline': ['Really good', 'Perfect Dress', 'Love it', 'Awesome'],
    'review_date': ['2013-01-14', '2014-04-22', '2015-07-28', '2015-06-12']
}

df = pd.DataFrame(data)

# Filter the DataFrame to include only the "Apparel" category
apparel_df = df[df['product_category'] == 'Apparel']

# Calculate average rating
average_rating = apparel_df['star_rating'].mean()

# Calculate standard error of the mean
std_error = apparel_df['star_rating'].std() / np.sqrt(len(apparel_df))

# Calculate z-score for 95% confidence interval
z_score = norm.ppf(0.975)  # 0.975 corresponds to 97.5% in the upper tail

# Calculate margin of error
margin_of_error = z_score * std_error

# Calculate confidence interval
lower_bound = average_rating - margin_of_error
upper_bound = average_rating + margin_of_error

# Print results
print("Average Rating:", average_rating)
print("Confidence Interval (95%):", (lower_bound, upper_bound))
