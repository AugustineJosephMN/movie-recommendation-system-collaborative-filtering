import pandas as pd
column_names = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv('u.data', sep='\t', names=column_names)
movie_titles = pd.read_csv("Movie_Id_Titles")
df = pd.merge(df,movie_titles,on='item_id')
ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
ratings['num of ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())
moviemat = df.pivot_table(index='user_id',columns='title',values='rating')

def movie_correlation(name):
    starwars_user_ratings = moviemat[name]
    similar_to_starwars = moviemat.corrwith(starwars_user_ratings)
    corr_liarliar = pd.DataFrame(similar_to_starwars,columns=['Correlation'])
    corr_liarliar.dropna(inplace=True)
    corr_liarliar = corr_liarliar.join(ratings['num of ratings'])
    new_pd=corr_liarliar[corr_liarliar['num of ratings']>100].sort_values('Correlation',ascending=False).head()
    movie_names = list(new_pd.index)
    print(movie_names)
    return movie_names

