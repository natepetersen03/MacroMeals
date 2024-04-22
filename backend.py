from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from flask_cors import CORS, cross_origin
from functools import reduce

db = SQLAlchemy()

app = Flask(__name__)
CORS(app)

# INSERT USERNAME HERE
username = ''

#INSERT PASSWORD HERE
password = ''

username_password = 'mysql+pymysql://' + username + ':' + password + '@'
server = "127.0.0.1"
db_name = "/macro_meals"

socket = "?unix_socket=/opt/local/var/run/mysql8/mysqld.sock"

app.config['SQLALCHEMY_DATABASE_URI'] = username_password + server + db_name + socket

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['CORS_HEADERS'] = 'Content-Type'

db.init_app(app)



class Recipe(db.Model):
    __tablename__ = 'recipes'
    name = db.Column(db.String, primary_key=True)
    ingredients = db.Column(db.String)
    directions = db.Column(db.String)
    calories = db.Column(db.Float)
    fat = db.Column(db.Float)
    saturated_fat = db.Column(db.Float)
    cholesterol = db.Column(db.Float)
    protein = db.Column(db.Float)
    carbohydrates = db.Column(db.Float)
    fiber = db.Column(db.Float)
    sugar = db.Column(db.Float)
    caffeine = db.Column(db.Float)
    quantity = db.Column(db.Float)
    link = db.Column(db.String)

@app.route("/search", methods=['GET'])
@cross_origin()
def search():
    try:
        calories_operator = request.args.get('caloriesOperator')
        calories_value = request.args.get('caloriesValue')

        fat_operator = request.args.get('fatOperator')
        fat_value = request.args.get('fatValue')

        saturated_fat_operator = request.args.get('saturatedFatOperator')
        saturated_fat_value = request.args.get('saturatedFatValue')
        
        cholesterol_operator = request.args.get('cholesterolOperator')
        cholesterol_value = request.args.get('cholesterolValue')        
        
        protein_operator = request.args.get('proteinOperator')
        protein_value = request.args.get('proteinValue')  
        
        carbohydrates_operator = request.args.get('carbohydratesOperator')
        carbohydrates_value = request.args.get('carbohydratesValue')
        
        fiber_operator = request.args.get('fiberOperator')
        fiber_value = request.args.get('fiberValue') 
        
        sugar_operator = request.args.get('sugarOperator')
        sugar_value = request.args.get('sugarValue')
        
        caffeine_operator = request.args.get('caffeineOperator')
        caffeine_value = request.args.get('caffeineValue')

        # using tuples since they are hashable
        result_sets = [
            {tuple(recipe.items()) for recipe in searchCalories(calories_operator, calories_value)},
            {tuple(recipe.items()) for recipe in searchFat(fat_operator, fat_value)},
            {tuple(recipe.items()) for recipe in searchSaturatedFat(saturated_fat_operator, saturated_fat_value)},
            {tuple(recipe.items()) for recipe in searchCholesterol(cholesterol_operator, cholesterol_value)},
            {tuple(recipe.items()) for recipe in searchProtein(protein_operator, protein_value)},
            {tuple(recipe.items()) for recipe in searchCarbohydrates(carbohydrates_operator, carbohydrates_value)},
            {tuple(recipe.items()) for recipe in searchFiber(fiber_operator, fiber_value)},
            {tuple(recipe.items()) for recipe in searchSugar(sugar_operator, sugar_value)},
            {tuple(recipe.items()) for recipe in searchCaffeine(caffeine_operator, caffeine_value)}
        ]
        
        # finding intersection of all lists
        recipe_text = list(reduce(lambda x, y: x & y, result_sets))
        
        # remapping back to a dictionary
        recipe_text = [{k: v for k, v in recipe} for recipe in recipe_text]
        
        # truncating to 500 entries
        return jsonify(recipe_text[:500])

    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text
    
# Below methods query the DB based on user input

def searchCalories(calories_operator, calories_value):
    if calories_value is None:
        recipes = db.session.query(Recipe).filter(
            Recipe.calories >= 0
        )
    elif calories_value.isdigit() and calories_value.strip() != "":
        calories_value = int(calories_value)
        if calories_operator == "<":
            recipes = db.session.query(Recipe).filter(
                Recipe.calories < calories_value
            )
        elif calories_operator == "=":
            recipes = db.session.query(Recipe).filter(
                Recipe.calories == calories_value
            )
        elif calories_operator == ">":
            recipes = db.session.query(Recipe).filter(
                Recipe.calories > calories_value
            )
        else:
            return jsonify({"error": "Invalid operator"}), 400
    else:
        recipes = db.session.query(Recipe).filter(
            Recipe.calories >= 0
        )
    return [{"name": recipe.name, "ingredients": recipe.ingredients, "directions": recipe.directions,
                    "calories": recipe.calories, "fat": recipe.fat, "saturated_fat": recipe.saturated_fat, 
                    "cholesterol": recipe.cholesterol, "protein": recipe.protein, "carbohydrates": recipe.carbohydrates,
                    "fiber": recipe.fiber, "sugar": recipe.sugar, "caffeine": recipe.caffeine,
                    "quantity": recipe.quantity, "link": recipe.link} for recipe in recipes]

def searchFat(fat_operator, fat_value):
    if fat_value is None:
        recipes = db.session.query(Recipe).filter(
            Recipe.fat >= 0
        )
    elif fat_value.isdigit() and fat_value.strip() != "":
        fat_value = int(fat_value)
        if fat_operator == "<":
            recipes = db.session.query(Recipe).filter(
                Recipe.fat < fat_value
            )
        elif fat_operator == "=":
            recipes = db.session.query(Recipe).filter(
                Recipe.fat == fat_value
            )
        elif fat_operator == ">":
            recipes = db.session.query(Recipe).filter(
                Recipe.fat > fat_value
            )
        else:
            return jsonify({"error": "Invalid operator"}), 400
    else:
        recipes = db.session.query(Recipe).filter(
            Recipe.fat >= 0
        )
    return [{"name": recipe.name, "ingredients": recipe.ingredients, "directions": recipe.directions,
                    "calories": recipe.calories, "fat": recipe.fat, "saturated_fat": recipe.saturated_fat, 
                    "cholesterol": recipe.cholesterol, "protein": recipe.protein, "carbohydrates": recipe.carbohydrates,
                    "fiber": recipe.fiber, "sugar": recipe.sugar, "caffeine": recipe.caffeine,
                    "quantity": recipe.quantity, "link": recipe.link} for recipe in recipes]

def searchSaturatedFat(saturated_fat_operator, saturated_fat_value):
    if saturated_fat_value is None:
        recipes = db.session.query(Recipe).filter(
            Recipe.saturated_fat >= 0
        )
    elif saturated_fat_value.isdigit() and saturated_fat_value.strip() != "":
        saturated_fat_value = int(saturated_fat_value)
        if saturated_fat_operator == "<":
            recipes = db.session.query(Recipe).filter(
                Recipe.saturated_fat < saturated_fat_value
            )
        elif saturated_fat_operator == "=":
            recipes = db.session.query(Recipe).filter(
                Recipe.saturated_fat == saturated_fat_value
            )
        elif saturated_fat_operator == ">":
            recipes = db.session.query(Recipe).filter(
                Recipe.saturated_fat > saturated_fat_value
            )
        else:
            return jsonify({"error": "Invalid operator"}), 400
    else:
        recipes = db.session.query(Recipe).filter(
            Recipe.saturated_fat >= 0
        )
    return [{"name": recipe.name, "ingredients": recipe.ingredients, "directions": recipe.directions,
                    "calories": recipe.calories, "fat": recipe.fat, "saturated_fat": recipe.saturated_fat, 
                    "cholesterol": recipe.cholesterol, "protein": recipe.protein, "carbohydrates": recipe.carbohydrates,
                    "fiber": recipe.fiber, "sugar": recipe.sugar, "caffeine": recipe.caffeine,
                    "quantity": recipe.quantity, "link": recipe.link} for recipe in recipes]

def searchCholesterol(cholesterol_operator, cholesterol_value):
    if cholesterol_value is None:
        recipes = db.session.query(Recipe).filter(
            Recipe.cholesterol >= 0
        )
    elif cholesterol_value.isdigit() and cholesterol_value.strip() != "":
        cholesterol_value = int(cholesterol_value)
        if cholesterol_operator == "<":
            recipes = db.session.query(Recipe).filter(
                Recipe.cholesterol < cholesterol_value
            )
        elif cholesterol_operator == "=":
            recipes = db.session.query(Recipe).filter(
                Recipe.cholesterol == cholesterol_value
            )
        elif cholesterol_operator == ">":
            recipes = db.session.query(Recipe).filter(
                Recipe.cholesterol > cholesterol_value
            )
        else:
            return jsonify({"error": "Invalid operator"}), 400
    else:
        recipes = db.session.query(Recipe).filter(
            Recipe.cholesterol >= 0
        )
    return [{"name": recipe.name, "ingredients": recipe.ingredients, "directions": recipe.directions,
                    "calories": recipe.calories, "fat": recipe.fat, "saturated_fat": recipe.saturated_fat, 
                    "cholesterol": recipe.cholesterol, "protein": recipe.protein, "carbohydrates": recipe.carbohydrates,
                    "fiber": recipe.fiber, "sugar": recipe.sugar, "caffeine": recipe.caffeine,
                    "quantity": recipe.quantity, "link": recipe.link} for recipe in recipes]

def searchProtein(protein_operator, protein_value):
    if protein_value is None:
        recipes = db.session.query(Recipe).filter(
            Recipe.protein >= 0
        )
    elif protein_value.isdigit() and protein_value.strip() != "":
        protein_value = int(protein_value)
        if protein_operator == "<":
            recipes = db.session.query(Recipe).filter(
                Recipe.protein < protein_value
            )
        elif protein_operator == "=":
            recipes = db.session.query(Recipe).filter(
                Recipe.protein == protein_value
            )
        elif protein_operator == ">":
            recipes = db.session.query(Recipe).filter(
                Recipe.protein > protein_value
            )
        else:
            return jsonify({"error": "Invalid operator"}), 400
    else:
        recipes = db.session.query(Recipe).filter(
            Recipe.protein >= 0
        )
    return [{"name": recipe.name, "ingredients": recipe.ingredients, "directions": recipe.directions,
                    "calories": recipe.calories, "fat": recipe.fat, "saturated_fat": recipe.saturated_fat, 
                    "cholesterol": recipe.cholesterol, "protein": recipe.protein, "carbohydrates": recipe.carbohydrates,
                    "fiber": recipe.fiber, "sugar": recipe.sugar, "caffeine": recipe.caffeine,
                    "quantity": recipe.quantity, "link": recipe.link} for recipe in recipes]

def searchCarbohydrates(carbohydrate_operator, carbohydrate_value):
    if carbohydrate_value is None:
        recipes = db.session.query(Recipe).filter(
            Recipe.carbohydrates >= 0
        )
    elif carbohydrate_value.isdigit() and carbohydrate_value.strip() != "":
        carbohydrate_value = int(carbohydrate_value)
        if carbohydrate_operator == "<":
            recipes = db.session.query(Recipe).filter(
                Recipe.carbohydrates < carbohydrate_value
            )
        elif carbohydrate_operator == "=":
            recipes = db.session.query(Recipe).filter(
                Recipe.carbohydrates == carbohydrate_value
            )
        elif carbohydrate_operator == ">":
            recipes = db.session.query(Recipe).filter(
                Recipe.carbohydrates > carbohydrate_value
            )
        else:
            return jsonify({"error": "Invalid operator"}), 400
    else:
        recipes = db.session.query(Recipe).filter(
            Recipe.carbohydrates >= 0
        )
    return [{"name": recipe.name, "ingredients": recipe.ingredients, "directions": recipe.directions,
                    "calories": recipe.calories, "fat": recipe.fat, "saturated_fat": recipe.saturated_fat, 
                    "cholesterol": recipe.cholesterol, "protein": recipe.protein, "carbohydrates": recipe.carbohydrates,
                    "fiber": recipe.fiber, "sugar": recipe.sugar, "caffeine": recipe.caffeine,
                    "quantity": recipe.quantity, "link": recipe.link} for recipe in recipes]

def searchFiber(fiber_operator, fiber_value):
    if fiber_value is None:
        recipes = db.session.query(Recipe).filter(
            Recipe.fiber >= 0
        )
    elif fiber_value.isdigit() and fiber_value.strip() != "":
        fiber_value = int(fiber_value)
        if fiber_operator == "<":
            recipes = db.session.query(Recipe).filter(
                Recipe.fiber < fiber_value
            )
        elif fiber_operator == "=":
            recipes = db.session.query(Recipe).filter(
                Recipe.fiber == fiber_value
            )
        elif fiber_operator == ">":
            recipes = db.session.query(Recipe).filter(
                Recipe.fiber > fiber_value
            )
        else:
            return jsonify({"error": "Invalid operator"}), 400
    else:
        recipes = db.session.query(Recipe).filter(
            Recipe.fiber >= 0
        )
    return [{"name": recipe.name, "ingredients": recipe.ingredients, "directions": recipe.directions,
                    "calories": recipe.calories, "fat": recipe.fat, "saturated_fat": recipe.saturated_fat, 
                    "cholesterol": recipe.cholesterol, "protein": recipe.protein, "carbohydrates": recipe.carbohydrates,
                    "fiber": recipe.fiber, "sugar": recipe.sugar, "caffeine": recipe.caffeine,
                    "quantity": recipe.quantity, "link": recipe.link} for recipe in recipes]

def searchSugar(sugar_operator, sugar_value):
    if sugar_value is None:
        recipes = db.session.query(Recipe).filter(
            Recipe.sugar >= 0
        )
    elif sugar_value.isdigit() and sugar_value.strip() != "":
        sugar_value = int(sugar_value)
        if sugar_operator == "<":
            recipes = db.session.query(Recipe).filter(
                Recipe.sugar < sugar_value
            )
        elif sugar_operator == "=":
            recipes = db.session.query(Recipe).filter(
                Recipe.sugar == sugar_value
            )
        elif sugar_operator == ">":
            recipes = db.session.query(Recipe).filter(
                Recipe.sugar > sugar_value
            )
        else:
            return jsonify({"error": "Invalid operator"}), 400
    else:
        recipes = db.session.query(Recipe).filter(
            Recipe.sugar >= 0
        )
    return [{"name": recipe.name, "ingredients": recipe.ingredients, "directions": recipe.directions,
                    "calories": recipe.calories, "fat": recipe.fat, "saturated_fat": recipe.saturated_fat, 
                    "cholesterol": recipe.cholesterol, "protein": recipe.protein, "carbohydrates": recipe.carbohydrates,
                    "fiber": recipe.fiber, "sugar": recipe.sugar, "caffeine": recipe.caffeine,
                    "quantity": recipe.quantity, "link": recipe.link} for recipe in recipes]

def searchCaffeine(caffeine_operator, caffeine_value):
    if caffeine_value is None:
        recipes = db.session.query(Recipe).filter(
            Recipe.caffeine >= 0
        )
    elif caffeine_value.isdigit() and caffeine_value.strip() != "":
        caffeine_value = int(caffeine_value)
        if caffeine_operator == "<":
            recipes = db.session.query(Recipe).filter(
                Recipe.caffeine < caffeine_value
            )
        elif caffeine_operator == "=":
            recipes = db.session.query(Recipe).filter(
                Recipe.caffeine == caffeine_value
            )
        elif caffeine_operator == ">":
            recipes = db.session.query(Recipe).filter(
                Recipe.caffeine > caffeine_value
            )
        else:
            return jsonify({"error": "Invalid operator"}), 400
    else:
        recipes = db.session.query(Recipe).filter(
            Recipe.caffeine >= 0
        )
    return [{"name": recipe.name, "ingredients": recipe.ingredients, "directions": recipe.directions,
                    "calories": recipe.calories, "fat": recipe.fat, "saturated_fat": recipe.saturated_fat, 
                    "cholesterol": recipe.cholesterol, "protein": recipe.protein, "carbohydrates": recipe.carbohydrates,
                    "fiber": recipe.fiber, "sugar": recipe.sugar, "caffeine": recipe.caffeine,
                    "quantity": recipe.quantity, "link": recipe.link} for recipe in recipes]


if __name__ == '__main__':
    app.run()
