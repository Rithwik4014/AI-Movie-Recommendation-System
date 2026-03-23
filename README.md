<div align="center">

# 🎬 AI Movie Recommendation System

<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
<img src="https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
<img src="https://img.shields.io/badge/NLP-Cosine%20Similarity-blueviolet?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge"/>

> **A machine learning-powered movie recommender** that uses NLP and cosine similarity to suggest movies you'll love — served through a sleek interactive Streamlit UI.

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [✨ Features](#-features)
- [🧠 How It Works](#-how-it-works)
- [📁 Repository Structure](#-repository-structure)
- [🚀 Getting Started](#-getting-started)
- [🛠️ Tech Stack](#-tech-stack)
- [📊 Dataset](#-dataset)
- [📷 App Preview](#-app-preview)
- [🤝 Contributing](#-contributing)

---

## 📌 Overview

The **AI Movie Recommendation System** is a content-based filtering application built with **Python**, **Scikit-learn**, and **Streamlit**. It analyzes movie metadata and finds similar movies using **Natural Language Processing (NLP)** and **Cosine Similarity**.

Whether you're a movie buff looking for your next watch or a developer exploring recommendation algorithms, this project has something for you!

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎯 **Content-Based Filtering** | Recommends movies similar to your choice based on metadata |
| 📈 **1000+ Movie Dataset** | Trained on a real dataset with 1000+ movie entries |
| 💬 **NLP Processing** | Uses CountVectorizer to convert text features into vectors |
| 🔍 **Cosine Similarity** | Measures similarity between movie vectors for accurate results |
| 🎨 **Interactive Streamlit UI** | Clean and user-friendly web interface |
| 💡 **Recommendation Explanation** | Shows why movies are being recommended |
| ⚡ **Fast & Lightweight** | Efficient similarity computation even for large datasets |

---

## 🧠 How It Works

<details>
<summary><b>Step 1: 💾 Data Loading & Preprocessing</b></summary>

- Loads the `movies.csv` dataset containing movie metadata
- Cleans and preprocesses text fields (genres, keywords, cast, crew, overview)
- Combines relevant features into a single "tags" column for NLP

</details>

<details>
<summary><b>Step 2: 📝 Vectorization with CountVectorizer</b></summary>

- Converts the combined text tags into numerical vectors
- Uses **Bag of Words** representation via `CountVectorizer`
- Applies stemming to normalize word variations

</details>

<details>
<summary><b>Step 3: 🔗 Cosine Similarity Computation</b></summary>

- Computes **cosine similarity** between all movie vectors
- Builds a similarity matrix for fast lookup
- Higher similarity score = more similar movies

</details>

<details>
<summary><b>Step 4: 🎬 Recommendation Generation</b></summary>

- User selects a movie from the Streamlit dropdown
- System fetches top N most similar movies from the matrix
- Returns recommendations with titles displayed in the UI

</details>

<details>
<summary><b>Step 5: 🎨 Streamlit UI Display</b></summary>

- Interactive web app built with **Streamlit**
- Movie selection via dropdown menu
- Displays top recommended movies in a clean layout

</details>

---

## 📁 Repository Structure

```
AI-Movie-Recommendation-System/
│
├── 🐍 app.py           # Main Streamlit application & recommendation logic
├── 📊 movies.csv       # Movie dataset (1000+ entries with metadata)
└── 📝 README.md        # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install pandas scikit-learn streamlit numpy
```

### Installation & Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Rithwik4014/AI-Movie-Recommendation-System.git
   cd AI-Movie-Recommendation-System
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   Or manually:
   ```bash
   pip install pandas scikit-learn streamlit numpy
   ```

3. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

4. **Open in browser:** Navigate to `http://localhost:8501`

5. **Select a movie** from the dropdown and click **Recommend** to get suggestions!

---

## 🛠️ Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)

</div>

| Technology | Role |
|---|---|
| **Python** | Core programming language |
| **Pandas** | Data loading and preprocessing |
| **Scikit-learn** | CountVectorizer & cosine similarity |
| **Streamlit** | Interactive web UI |
| **NumPy** | Numerical operations |

---

## 📊 Dataset

The `movies.csv` file contains metadata for **1000+ movies** including:

| Column | Description |
|---|---|
| `movie_id` | Unique identifier for each movie |
| `title` | Movie title |
| `overview` | Plot summary / description |
| `genres` | Movie genres (Action, Comedy, Drama, etc.) |
| `keywords` | Associated keywords |
| `cast` | Lead cast members |
| `crew` | Director and key crew |

> 💡 All text features are combined into a single "tags" field for vectorization.

---

## 📷 App Preview

> ▶️ Run `streamlit run app.py` to launch the app locally and explore movie recommendations interactively.

**Sample Workflow:**
```
1. Open the app in your browser
2. Select a movie (e.g., "The Dark Knight")
3. Click "Recommend"
4. Get top 5 similar movies instantly!
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can improve the project:

- 📊 Add movie posters using TMDB API
- 🔍 Implement collaborative filtering
- 🌟 Add user ratings and reviews
- 💾 Expand the dataset

**Steps to Contribute:**
1. Fork this repository
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -m 'Add: your feature'`
4. Push: `git push origin feature/your-feature`
5. Open a **Pull Request**

---

<div align="center">

**Made with ❤️ by [Rithwik4014](https://github.com/Rithwik4014)**

⭐ *If you found this useful, please give it a star!* ⭐

![Python](https://img.shields.io/badge/Built%20with-Python%20%26%20Streamlit-blue?style=flat-square)

</div>
