from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

db = SQLAlchemy()

app = Flask(__name__)

username_password = 'mysql+pymysql://root:NaTe6283!@'
server = "127.0.0.1"
db_name = "/macro_meals"

socket = "?unix_socket=/opt/local/var/run/mysql8/mysqld.sock"

app.config['SQLALCHEMY_DATABASE_URI'] = username_password + server + db_name + socket

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)



class Recipe(db.Model):
    __tablename__ = 'recipes'
    name = db.Column(db.String, primary_key=True)
    ingredients = db.Column(db.String)
    directions = db.Column(db.String)
    calories = db.Column(db.Float)
    fat = db.Column(db.String)
    saturated_fat = db.Column(db.String)
    cholesterol = db.Column(db.String)
    protein = db.Column(db.String)
    carbohydrates = db.Column(db.String)
    fiber = db.Column(db.String)
    sugar = db.Column(db.String)
    caffeine = db.Column(db.String)
    quantity = db.Column(db.String)
    link = db.Column(db.String)

@app.route("/")
def index():
    try:
        recipes = db.session.query(Recipe).filter(
            Recipe.calories < 250
        )
        recipe_text = '<ul>'
        for recipe in recipes:
            recipe_text += '<li>' + recipe.name + ', ' + recipe.ingredients + '</li>'
        recipe_text += '</ul>'
        return recipe_text
    

    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

if __name__ == '__main__':
    app.run()
