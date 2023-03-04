import pickle
import streamlit as st
import requests
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🆚",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://vishalydv.netlify.app/',
        'Report a bug': "https://vishalydv.netlify.app/",
        'About': "This is developed by Vishal Yadav. This is extremely a good place where you can get good recommendations about the best movies. "
    }
)
# st.markdown(
#          f"""
#          <style>
#          .stApp {{
#              background: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNc0PEhDpCbwUit34_hoROhmlN9m1j7QRH8w&usqp=CAU");
#              background-size: cover
#          }}
#          </style>
#          """,
#          unsafe_allow_html=True
#      )
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender System')
movies = pickle.load(open('models/movie_list.pkl','rb'))
similarity = pickle.load(open('models/similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

    

ft = """
<style>
a:link , a:visited{
color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness*/
background-color: transparent;
text-decoration: none;
}

a:hover,  a:active {
color: #0283C3; /* theme's primary color*/
background-color: transparent;
text-decoration: underline;
}

#page-container {
  position: relative;
  min-height: 10vh;
}

footer{
    visibility:hidden;
}

.footer {
position: relative;
left: 0;
top:230px;
bottom: 0;
width: 100%;
background-color: transparent;
color: #808080; /* theme's text color hex code at 50 percent brightness*/
text-align: left; /* you can replace 'left' with 'center' or 'right' if you want*/
}
</style>

<div id="page-container">

<div class="footer">
<p style='font-size: 0.9em;'>Made 
with <img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height= "15"/> by <a style='display: inline; text-align: left;' href="https://vishalydv.netlify.app/" target="_blank"> Vishal Yadav</a></p>
</div>

</div>
"""
st.write(ft, unsafe_allow_html=True)