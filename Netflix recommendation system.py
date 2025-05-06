import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv("netflix_cleaned.csv")

# Streamlit App
st.set_page_config(page_title="Netflix Dataset Explorer", layout="wide")

st.title("📺 Netflix Dataset Explorer")

# Show raw data
if st.checkbox("Show Raw Data"):
    st.write(df)

# Basic dataset info
st.subheader("Dataset Summary")
st.write("Number of rows:", df.shape[0])
st.write("Number of columns:", df.shape[1])
st.write("Column names:", df.columns.tolist())

# Search by title
st.subheader("🔍 Search for a Genres")
search_term = st.text_input("Enter a title or keyword:")
if search_term:
    results = df[df['genres'].str.contains(search_term, case=False, na=False)]
    st.write(f"Found {len(results)} results:")
    st.write(results)

# Filter by type
st.subheader("🎞 Filter by Type")
selected_type = st.selectbox("Select Type", df['type'].dropna().unique())
filtered = df[df['type'] == selected_type]
st.write(f"{len(filtered)} {selected_type} entries")
st.write(filtered.head(10))

# Visualize country distribution
st.subheader("🌍 Top 10 Countries by Content")
top_countries = df['country'].value_counts().head(10)
st.bar_chart(top_countries)

# Year distribution
st.subheader("📅 Release Year Distribution")
if 'release_year' in df.columns:
    st.line_chart(df['release_year'].value_counts().sort_index())

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")






