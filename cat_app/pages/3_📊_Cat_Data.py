# pages/3_📊_Cat_Data.py - Plotly-free version
import streamlit as st
import pandas as pd
import numpy as np
# Remove or comment out: import plotly.express as px

st.title("📊 Global Cat Statistics Dashboard")

tab1, tab2, tab3 = st.tabs(["🐾 Breed Popularity", "📈 Cat Demographics", "🗺️ Geographic Distribution"])

with tab1:
    st.header("Most Popular Cat Breeds 2024")
    
    breed_data = pd.DataFrame({
        "Breed": ["Domestic Shorthair", "Maine Coon", "Ragdoll", "British Shorthair", "Siamese", 
                  "Persian", "Sphynx", "Bengal", "Scottish Fold", "Russian Blue"],
        "Popularity": [35, 22, 18, 15, 12, 10, 8, 7, 5, 4],
        "Avg Lifespan": [15, 13, 15, 14, 15, 14, 13, 14, 12, 15],
        "Shedding": ["Medium", "High", "Medium", "High", "Low", "High", "None", "Low", "Medium", "Low"]
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Top 8 Breeds by Popularity")
        # Use Streamlit's native bar chart
        chart_data = breed_data.head(8).set_index('Breed')['Popularity']
        st.bar_chart(chart_data)
    
    with col2:
        st.subheader("✏️ Edit Breed Data")
        edited_df = st.data_editor(
            breed_data,
            column_config={
                "Popularity": st.column_config.NumberColumn("Popularity Score", min_value=0, max_value=100),
                "Avg Lifespan": st.column_config.NumberColumn("Lifespan (years)", min_value=0, max_value=30),
            },
            hide_index=True,
            key="breed_editor"
        )
        
        if st.button("📥 Download Edited Data"):
            csv = edited_df.to_csv(index=False)
            st.download_button("Download CSV", csv, "cat_breeds.csv", "text/csv")

with tab2:
    st.header("Cat Demographics Analysis")
    
    np.random.seed(42)
    n_cats = 1000
    demo_data = pd.DataFrame({
        "Age": np.random.normal(5, 3, n_cats).clip(0, 20),
        "Weight_kg": np.random.normal(4.5, 1.5, n_cats).clip(2, 10),
        "Gender": np.random.choice(["Male", "Female"], n_cats, p=[0.52, 0.48]),
        "Neutered": np.random.choice(["Yes", "No"], n_cats, p=[0.85, 0.15])
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Age Distribution")
        # Use Streamlit's native histogram approach
        age_hist = np.histogram(demo_data['Age'], bins=30)
        hist_df = pd.DataFrame({
            'Age Range': [f"{age_hist[1][i]:.1f}-{age_hist[1][i+1]:.1f}" for i in range(len(age_hist[1])-1)],
            'Count': age_hist[0]
        })
        st.bar_chart(hist_df.set_index('Age Range'))
    
    with col2:
        st.subheader("Age vs Weight")
        # Use Streamlit's native scatter chart
        scatter_data = demo_data[['Age', 'Weight_kg']].copy()
        st.scatter_chart(scatter_data, x='Age', y='Weight_kg')
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Average Age", f"{demo_data['Age'].mean():.1f} years")
    with col2:
        st.metric("Average Weight", f"{demo_data['Weight_kg'].mean():.1f} kg")
    with col3:
        st.metric("Male/Female Ratio", f"{52}/{48}")
    with col4:
        st.metric("Neutered Rate", "85%")

with tab3:
    st.header("Where Cats Rule the World")
    
    geo_data = pd.DataFrame({
        "Country": ["USA", "China", "Russia", "Brazil", "France", "Japan", "UK", "Germany", "Italy", "Canada"],
        "Cat Population (millions)": [94.2, 53.1, 22.8, 22.1, 14.9, 9.8, 9.6, 9.2, 7.5, 7.3],
        "Cats per 100 people": [28, 4, 16, 10, 23, 8, 14, 11, 12, 20]
    })
    
    # Use Streamlit's native map for geographic data
    st.subheader("Global Cat Population (Millions)")
    st.bar_chart(geo_data.set_index('Country')['Cat Population (millions)'])
    
    st.dataframe(geo_data.sort_values("Cat Population (millions)", ascending=False), 
                 hide_index=True, use_container_width=True)