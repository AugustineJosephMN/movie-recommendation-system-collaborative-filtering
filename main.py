from Recommender import movie_correlation
import pandas as pd
from flask import Flask, render_template, request

movie_titles = pd.read_csv("Movie_Id_Titles")

# defining a function that recommends 10 most similar movies
def rcmd(m):
    # check if the movie is in our database or not
    if m not in movie_titles['title'].unique():
        print(m)
        print(movie_titles['title'])
        print("nope")
        return('This movie is not in our database.\nPlease check if you spelled it correct.')
    else:
        list=movie_correlation(m)
        lst = list[:9]
        return lst


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/recommend")
def recommend():
    movie = request.args.get('movie')
    r = rcmd(movie)
    movie = movie.upper()
    if type(r)==type('string'):
        return render_template('recommend.html',movie=movie,r=r,t='s')
    else:
        return render_template('recommend.html',movie=movie,r=r,t='l')



if __name__ == '__main__':
    app.run()
