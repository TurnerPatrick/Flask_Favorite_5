# Import the app variable from the init
from fav_artists_app import app

# Import specific packages from flask
from flask import render_template

# Default Home Route
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/artists')
def artistsRoute():
    names = ['Inga Marchand','Derrick Rose','Tracy McGrady','Nasir Jones']
    return render_template('artists.html',list_names = names)