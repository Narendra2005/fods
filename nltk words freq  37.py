import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import string
from nltk.corpus import stopwords

# Download stopwords if not already downloaded
import nltk
nltk.download('stopwords')

# Load dataset from CSV
df = pd.read_csv('data.csv')

# Preprocess the text data
stop_words = set(stopwords.words('english'))
word_freq = Counter()
for feedback in df['feedback']:
    # Remove punctuation and convert to lowercase
    feedback = feedback.translate(str.maketrans('', '', string.punctuation)).lower()
    # Remove stopwords and count frequencies
    word_freq.update(word for word in feedback.split() if word not in stop_words)

# Ask user for N
N = int(input("Enter the number of top words to display: "))

# Display top N most frequent words and their frequencies
top_words = word_freq.most_common(N)
print("\nTop", N, "most frequent words:")
for word, freq in top_words:
    print(word, ":", freq)

# Plot a bar graph
words, frequencies = zip(*top_words)
plt.figure(figsize=(10, 6))
plt.bar(words, frequencies, color='skyblue')
plt.xlabel('Words')
plt.ylabel('Frequencies')
plt.title('Top {} Most Frequent Words'.format(N))
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
