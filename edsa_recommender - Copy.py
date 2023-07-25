"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Welcome","About Us","Uncovering Patterns of Movie Data", "Recommender System","Solution Overview"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
    if page_selection == "About Us":
        st.title("About Us")
        st.markdown('<div style="text-align: justify;">We are CineAI and we provide better movie recommendations to you</div>', unsafe_allow_html=True)
        st.subheader("Vision")
        st.markdown('<div style="text-align: justify;">Our vision at CineAI is to revolutionize the entertainment industry by harnessing the power of artificial intelligence and technology to create immersive, personalized, and captivating cinematic experiences. We envision a future where AI-driven advancements enhance storytelling, elevate visual effects, and redefine the way people engage with movies, making every cinematic moment an extraordinary journey</div>', unsafe_allow_html=True)
        st.image('resources/imgs/cineai Logo.png')
        
    if page_selection == "Uncovering Patterns of Movie Data":
        st.title("Uncovering Patterns of Movie Data")
        genre_df = pd.read_csv('resources/data/genrecount.csv')
        #st.bar_chart(data=None, *, x=None, y=None, width=0, height=0, use_container_width=True)
        #st.bar_chart(genre_df, x = 'Genre', y = 'No of ratings')
        #This section is for a pie chart 
        #import streamlit as st
        import matplotlib.pyplot as plt

        
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        
        # Use Markdown syntax with CSS styling for the subheader
        st.markdown('<h3 style="text-align: center;">Distribution of Movie Genres</h3>', unsafe_allow_html=True)

        # Rest of your Streamlit app code

        #st.subheader("Distribution of Movie Genres")
        labels = genre_df['Genre']
        sizes = genre_df['No of ratings']
        #explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
        
        # Determine the threshold for displaying labels
        threshold = sum(sizes) * 0.01

        # Create a list of labels with a condition to display only for sizes above the threshold
        labels_selected = [n if v > threshold else '' for n, v in zip(labels, sizes)]

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels_selected, autopct=lambda x: '{:2.0f}%'.format(x) if x > 1 else '',
                shadow=False, startangle=0)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        st.pyplot(fig1)

        st.markdown('<h3 style="text-align: center;">Top Ten High Rated Movies in Drama Genre</h3>', unsafe_allow_html=True)
        titles_df = pd.read_csv('resources/data/topdrama_titles.csv')
        st.bar_chart(titles_df, x = 'Movie Title', y = 'Rating')

        st.markdown('<h3 style="text-align: center;">Count of Number of Movies Released Each Year(from 1990)</h3>', unsafe_allow_html=True)
        filtered_df = pd.read_csv('resources/data/movies_year_summary.csv')
        st.line_chart(data=filtered_df , x='Year', y='Number of Movies', use_container_width=True)
        #st.line_chart(data=year_counts , width=12, height= 6, use_container_width=True)
    if page_selection == "Welcome":
          def get_img_as_base64(file):
            with open(file, "rb") as f:
                data = f.read()
            return base64.b64encode(data).decode()
          img = get_img_as_base64("tv-screens2.gif")
          page_bg_img = f"""
        <style>
        [data-testid="stAppViewContainer"] > .main {{
        background-image: url("data:image/png;base64,{img}");
        background-size: 100%;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        }}
        </style>
        """
          st.markdown(page_bg_img, unsafe_allow_html=True)
          st.title("Welcome to CineAI")
          st.subheader("Synchronizing Cinema with Artificial Intelligence")
          st.write("Elevate Your Movie Experience with Cutting-Edge AI Innovation!")
        
                








if __name__ == '__main__':
    main()
