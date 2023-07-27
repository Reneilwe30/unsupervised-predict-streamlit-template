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
#from bokeh.models.widgets import Div
import streamlit.components.v1 as components

# Data handling dependencies
import pandas as pd
import numpy as np
import base64

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model
from PIL import Image 
import plotly.express as px

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Welcome","About Us","Uncovering Patterns of Movie Data", "Recommender System","Solution Overview", "Coming Soon"]

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
        @st.cache_data
        #st.title("Solution Overview")  
        def get_img_as_base64(file):
            with open(file, "rb") as f:
                data = f.read()
            return base64.b64encode(data).decode()


        img2 = get_img_as_base64("resources/imgs/bgimg2.png")

        page_bg_img = f"""
        <style>
        [data-testid="stAppViewContainer"] > .main {{
        background-image: url("data:image/png;base64,{img2}");
        background-size: 100%;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        }}
        </style>
        """

        st.markdown(page_bg_img, unsafe_allow_html=True)
        st.title("Solution Overview")

        st.write("At CineAI, we have developed an exceptional solution that redefines how movies are recommended to you. Our advanced recommender systems combine the power of content-based filtering, collaborative filtering, and the Singular Value Decomposition (SVD) model to deliver accurate and personalized movie suggestions, perfectly tailored to your unique preferences.")

        st.write("Content-Based Filtering:") 
        st.write("Our content-based filtering technique revolves around understanding the characteristics and attributes of movies you've enjoyed in the past. By analyzing movie metadata, such as genres, actors, directors, and plot summaries, we create a profile that reflects your movie tastes. Using this information, our system recommends movies with similar attributes, ensuring that you discover films that resonate with your interests.")

        st.write("Collaborative Filtering:")
        st.write("Collaborative filtering focuses on finding patterns in movie ratings and user behavior. By analyzing the preferences of users similar to you, we identify movies that others with similar tastes have enjoyed but that you might not have seen yet. This collaborative approach ensures that you're exposed to a diverse range of films, increasing the likelihood of discovering hidden gems and expanding your movie horizons.")

        st.write("Singular Value Decomposition (SVD) Model:")
        st.write("Incorporating the SVD model, our solution digs even deeper into your movie-watching history. This mathematical technique helps uncover latent factors that influence your movie preferences, revealing subtle patterns that may not be obvious through traditional methods. The SVD model allows us to make precise predictions on how you'll rate movies you haven't seen, enhancing the accuracy of our recommendations.")

        image = Image.open("resources/imgs/AI human interact.png")
        st.image(image, width=150)

        st.write("The magic of our solution lies in how we seamlessly blend these three techniques to provide you with a comprehensive and highly personalized movie-watching experience. Our solution continuously learns and adapts as you interact with it, refining its recommendations over time. The more you use our platform, the better it understands your unique tastes, making each movie recommendation even more accurate and enjoyable.")
        st.write("By implementing our solution, businesses can boost user engagement, drive customer satisfaction, and increase platform affinity. For users, our solution opens the doors to a treasure trove of movies that perfectly match their interests, making their movie-watching experience more delightful and fulfilling.")

        st.write("Discover the power of personalized movie recommendations with CineAI. Connect with us today and embark on an unforgettable cinematic journey tailored to you.")

        st.subheader("Get in touch with us")

        with st.form("contact_info"):
            my_name = st.text_input("Name and Surname")
            my_email = st.text_input("Email address")
            my_message = st.text_input("Write Message Here")
            st.form_submit_button('Submit')

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
    if page_selection == "About Us":
        @st.cache_data
        def get_img_as_base64(file):
            with open(file, "rb") as f:
                data = f.read()
            return base64.b64encode(data).decode()


        img1 = get_img_as_base64("resources/imgs/bgimg1.gif")

        page_bg_img = f"""
        <style>
        [data-testid="stAppViewContainer"] > .main {{
        background-image: url("data:image/png;base64,{img1}");
        background-size: 100%;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        }}
        </style>
        """

        st.markdown(page_bg_img, unsafe_allow_html=True)
        st.title("About Us")
        #image = Image.open("filmstrip.png")
        #st.image(image)
        st.write("At CineAI, we are passionate about movies and believe that everyone deserves an extraordinary cinematic experience. We are an AI company specializing in building advanced recommender systems to help you find the perfect movies that align with your unique preferences.")
        st.write("In today's digital world, where there are countless movie options available, we understand that it can be overwhelming to choose what to watch.That's where CineAI comes in. Our team consists of AI experts and movie enthusiasts who work tirelessly to create intelligent algorithms that truly understand your movie tastes.")
        st.write("Innovation is at the core of our work at CineAI. We constantly stay ahead of the latest trends in AI technology, exploring new techniques and refining our algorithms to provide you with the best movie recommendations. Our dedicated team is committed to creating an exceptional movie-watching experience for you.")

        st.subheader("Meet the team")

        imi = Image.open("resources/imgs/imi1.png")
        renei = Image.open("resources/imgs/reneilwe1.png")
        olwe = Image.open("resources/imgs/olwethu1.png")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.image(imi,use_column_width=False, clamp=False, width = 150, output_format="png")
            st.write("Ntokozo Imi Bingwa")
            st.write("Lead Data Scientist")

        with col2:
            st.image(renei,use_column_width=False, clamp=False, width = 150, output_format="png")
            st.write("Reneilwe Motsamai")
            st.write("Lead Data Engineer")

        with col3:
            st.image(olwe,use_column_width=False, clamp=False, width = 150, output_format="png")
            st.write("Olwethu Magadla")
            st.write("Data Engineer")

        baart = Image.open("resources/imgs/baartman1.png")
        anto = Image.open("resources/imgs/antonia1.png")
        judy = Image.open("resources/imgs/judy1.png")
        thato = Image.open("resources/imgs/thato1.png")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.image(baart,use_column_width=False, clamp=False, width = 150, output_format="png")
            st.write("Mathapelo Baartman")
            st.write("Data Scientist")

        with col2:
            st.image(anto,use_column_width=False, clamp=False, width = 150, output_format="png")
            st.write("Antonia Bardo")
            st.write("Data Analyst")

        with col3:
            st.image(judy,use_column_width=False, clamp=False, width = 150, output_format="png")
            st.write("Sinyosi Judy")
            st.write("Data Scientist") 
         
         

        col1, col2, col3 = st.columns(3)

        with col1:
            st.image(thato,use_column_width=False, clamp=False, width = 150, output_format="png")
            st.write("Thato Matlou")
            st.write("Data Scientist") 

        st.write(" ")

        st.write("Discover incredible films that resonate with you, uncover hidden gems, and immerse yourself in a world of captivating storytelling. At CineAI, we are here to transform your movie experience and bring you closer to the movies you love.")
        st.write("Welcome to CineAI, where movies and AI converge to create an enchanting world of cinematic discovery.")

        image = Image.open("resources/imgs/cineai Logo.png")
        st.image(image, width=250, caption="Powered by: CineAI")
        
    if page_selection == "Uncovering Patterns of Movie Data":
        st.title("Uncovering Patterns of Movie Data")
        #st.markdown('<h3 style="text-align: center;">Number of Movies Released Each Year(from 1990)</h3>', unsafe_allow_html=True)
        #filtered_df = pd.read_csv('resources/data/movies_year_summary.csv')
        #st.line_chart(data=filtered_df , x='Year', y='Number of Movies', use_container_width=True)
        #st.line_chart(data=year_counts , width=12, height= 6, use_container_width=True)'''

        #st.markdown('<h3 style="text-align: center;">Top Ten Directors with Most Rated Movies</h3>', unsafe_allow_html=True)
        top_directors_df = pd.read_csv("resources/data/top_10_directors_most_rated_movies.csv")
        #st.bar_chart(top_directors_df, x = 'Number of Movies Released', y = 'Directors') 

        #Top Ten Directors
        st.markdown("""<h3 style="text-align: center;">Top Ten Directors with Most Released Movies</h3><p style="text-align: center;"></p>""", unsafe_allow_html=True)
        fig_top_directors=px.bar(top_directors_df,x='Number of Movies Released',y='Directors', orientation='h')
        fig_top_directors.update_traces(marker_color='green',  # Change the bar color
                      textfont_color='black',  # Change the label text color
                      hovertemplate='<b>Directors : %{y}</b><br><b>Number of Movies Released: %{x}</b>',  # Change the tooltip text
                      selector=dict(type='bar'))  # Select only the bar traces
        st.write(fig_top_directors)

        st.markdown('<h3 style="text-align: center;">Top 5 Movies Directed by Luc Besson</h3>', unsafe_allow_html=True)
        movie_ratings_df = pd.read_csv("resources/data/luc_besson_movies.csv")
        st.bar_chart(movie_ratings_df, x = 'Movie Titles', y = 'Ratings') 

       
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
        
        #with st.expander("See explanation"):
           # st.write(\"\"\"
                #The chart above shows some numbers I picked for you.
                #I #rolled actual dice for these, so they're *guaranteed* to
                #be random.
            #\"\"\")'''
        

        st.markdown('<h3 style="text-align: center;">Top Ten High Rated Movies in Drama Genre</h3>', unsafe_allow_html=True)
        titles_df = pd.read_csv('resources/data/topdrama_titles.csv')
        st.bar_chart(titles_df, x = 'Movie Title', y = 'Rating')

    if page_selection == "Welcome":
          @st.cache_data
          def get_img_as_base64(file):
            with open(file, "rb") as f:
                data = f.read()
            return base64.b64encode(data).decode()
          img = get_img_as_base64("resources/imgs/tv-screens2.png")
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
    if page_selection == "Coming Soon":
        @st.cache_data
        def get_img_as_base64(file):
            with open(file, "rb") as f:
                data = f.read()
            return base64.b64encode(data).decode()


        img3 = get_img_as_base64("resources/imgs/bgimg3.gif")

        page_bg_img = f"""
        <style>
        [data-testid="stAppViewContainer"] > .main {{
        background-image: url("data:image/png;base64,{img3}");
        background-size: 100%;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        }}
        </style>
        """

        st.markdown(page_bg_img, unsafe_allow_html=True)
        st.title("Coming Soon")
        st.write("Check out what the upcoming movie releases are and set a date to watch your most anticipated movie releases.")

        

        if st.button('Go to Upcoming Releases'):
            components.iframe("https://www.ign.com/upcoming/movies", height=800, scrolling=True)  # Current tab
        

if __name__ == '__main__':
    main()
