import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample music dataset
data = {
    'title': ['Song 1', 'Song 2', 'Song 3', 'Song 4', 'Song 5'],
    'artist': ['Artist A', 'Artist B', 'Artist A', 'Artist C', 'Artist D'],
    'genre': ['Pop', 'Rock', 'Pop', 'Jazz', 'Pop'],
}

music_df = pd.DataFrame(data)

# Create a TF-IDF vectorizer to convert text data into numerical vectors
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
music_df['description'] = music_df['artist'] + ' ' + music_df['genre']

tfidf_matrix = tfidf_vectorizer.fit_transform(music_df['description'])

# Compute the cosine similarity between items (songs)
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

def get_recommendations(title, cosine_sim=cosine_sim):
    idx = music_df.index[music_df['title'] == title].tolist()[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]  # Get the top 3 similar songs (excluding itself)
    song_indices = [i[0] for i in sim_scores]
    return music_df['title'].iloc[song_indices]

# Example usage:
user_input = 'Song 1'
recommendations = get_recommendations(user_input)
print(f"Recommended songs for '{user_input}':")
for song in recommendations:
    print(song)
