import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="AI Movie Recommender", layout="centered")

st.markdown("<h1 style='text-align: center;'>🎬 AI Movie Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: grey;'>Using Real Dataset + Machine Learning</p>", unsafe_allow_html=True)

st.divider()

# Load dataset
data = pd.read_csv("movies.csv")

# Fix: use 'cast' column instead of overview
data = data[['title', 'cast']].dropna()

# Convert text
data['cast'] = data['cast'].astype(str)

# Limit data
data = data.head(1000)

# ML
cv = CountVectorizer(max_features=3000, stop_words='english')
matrix = cv.fit_transform(data['cast'])
similarity = cosine_similarity(matrix)

# UI
selected_movie = st.selectbox("🎯 Select a movie", data['title'].values)

def recommend(movie):
    idx = data[data['title'] == movie].index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]
    return [data.iloc[i[0]].title for i in scores]

if st.button("🚀 Recommend Movies"):
    results = recommend(selected_movie)

    st.subheader("✨ Recommendations")
    for movie in results:
        st.success(movie)

    st.session_state["results"] = results

# Explanation
if "results" in st.session_state:
    if st.button("🤖 Explain"):
        st.write(f"""
These movies are recommended based on similarity in cast and production features.

Machine learning techniques like **CountVectorizer** and **Cosine Similarity** are used to find patterns and suggest similar movies.
""")