from Class_Objects.movies import Movie
from Fresh_Tomatoes.fresh_tomatoes import open_movies_page


#creating class instances/ objects with their corresponding 'title', 'poster_image_url' 
#and 'trailer_youtube_url' member values - to be used by the 'open_movies_page()' function.
bionicle = Movie(
	'Bionicle The Mask of Light', 
	'http://ecx.images-amazon.com/images/I/511HT4HNZWL.jpg', 
	'https://www.youtube.com/watch?v=RwDqw-z_IfY', 'Released 2003 - my favourite nostalgic film from my youth')

napoleonDyamite = Movie(
	'Napoleon Dynamite',
	'http://www.circlecinema.com/wp-content/uploads/2011/09/napoleon-dynamite-poster.jpg',
	'https://www.youtube.com/watch?v=ZHDi_AnqwN4', 'Released 2004 - Pretty much the best movie ever. GOSH' )

hotRod = Movie (
	'Hot Rod',
	'http://oneguyrambling.com/wp-content/uploads/2011/12/Hot-Rod.jpg',
	'https://www.youtube.com/watch?v=evQBZhJ3qX8', 'Released 2007 - he, who is resistant to change is destined to perish - Dave')


#creating a list to store 'Movie' instacnes because 'open_movies_page' expects a
#a list of objects as it's only argument.
movies = [bionicle, napoleonDyamite, hotRod]

#Giving 'open_movies_page' the 'movies' list.
open_movies_page(movies)