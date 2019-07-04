import os
import env
from flask import Flask, render_template, request, url_for, redirect, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
import bcrypt

# create an instance of Flask
app = Flask(__name__)

# before deploying convert to enviroment variable
app.config["MONGO_DBNAME"] = 'CookBook'
app.config['MONGO_URI'] = os.environ.get('MONGODB_URI')

# we create an instance of Mongo
mongo = PyMongo(app)

# secret key needed to create session cookies / before deploying convert to enviroment variable
app.secret_key = "randomString123"



# https://www.youtube.com/watch?v=vVx1737auSE
# landing page for the website for new users. 
@app.route('/')
def index():
   
    # if the cookie for the user already exist the login page is skipped
    if "username" in session:
        return redirect(url_for('get_recipes'))
    
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.Users
    user_login = users.find_one({'author':request.form['username']})

    if user_login:
        if request.form['password'] == user_login['password']:
            session["username"] = request.form["username"]
            return redirect(url_for('get_recipes'))
        
    return 'The username and/or password are not correct!'

@app.route('/register', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.Users
        user_exists = users.find_one({'author':request.form['username']})

        if user_exists is None:
            users.insert({'author':request.form['username'], 'password':request.form['password']})
            session['username'] = request.form['username']
            return redirect(url_for('get_recipes'))

        return 'That username already exists, please try with a different one.'

    return render_template('register.html')

#function to get the username at anytime when the user is logged in
def getusername():
    username = session['username']
    return username

#function use to convert strings separated by commas to arrays
def string_to_array(string):
    array = string.split("\n")
    return array

#home page
@app.route('/get_recipes')
def get_recipes():
    username = getusername()
    return render_template('get_recipes.html', username=username, recipes = mongo.db.Recipes.find())

# function to add new recipe
@app.route('/add_recipe')
def add_recipe():
    categories = mongo.db.Categories.find()
    cuisines = mongo.db.Cuisines.find()
    difficulty = mongo.db.Difficulty.find()
    return render_template('add_recipe.html', categories = categories, cuisines=cuisines, difficulty=difficulty)

# function to see and insert new categories or cuisines
@app.route('/manage_categories')
def manage_categories():
    recipes = mongo.db.Recipes.find()
    categories = mongo.db.Categories.find()
    cuisines = mongo.db.Cuisines.find()
    category_object=[]
    cuisine_object=[]

    for category in categories:
	    count_recipes_category = mongo.db.Recipes.find({'category':category['category']}).count()
	    category_object.append({"category_id" : category['_id'] ,"category" : category['category'], "count_recipes_category" : count_recipes_category})
        
    for cuisine in cuisines:
	    count_recipes_cuisine = mongo.db.Recipes.find({'cuisine':cuisine['cuisine']}).count()
	    cuisine_object.append({"cuisine_id" : cuisine['_id'], "cuisine" : cuisine['cuisine'], "count_recipes_cuisine" : count_recipes_cuisine} )

    return render_template('manage_categories.html', categories = category_object, cuisines = cuisine_object)

# funtion to insert into the database the new recipe
@app.route('/insert_recipe', methods=['GET', 'POST'])
def insert_recipe():
    recipes = mongo.db.Recipes  
    recipes.insert_one({
            'recipe_name':request.form['recipe_name'].capitalize(),
            'instructions':string_to_array(request.form['instructions']),
            'serves':request.form['serves'],
            'calories':request.form['calories'],
            'difficulty_level':request.form['difficulty_level'],
            'cooking_time':request.form['cooking_time'],
            'cuisine':request.form['cuisine'],
            'allergens':string_to_array(request.form['allergens']),
            'ingredients':string_to_array(request.form['ingredients']),
            'image_url':request.form['image_url'],
            'author':getusername().capitalize(),
            'upvotes':0,
            'date':datetime.now().strftime("%d/%m/%Y"),
            'category':request.form['category']
        })
    return redirect(url_for('get_recipes'))

# function to see a recipe after clicking on its image or "view" link
@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    recipe = mongo.db.Recipes.find_one({"_id":ObjectId(recipe_id)})
    return render_template('view_recipe.html', recipe = recipe, username = getusername())

# function to vote the recipes (the recipe author is not allowed to vote)
@app.route('/view_recipe/vote/<recipe_id>')
def vote(recipe_id):
    mongo.db.Recipes.update_one({"_id":ObjectId(recipe_id)}, {'$inc': {'upvotes': 1}})
    return redirect(url_for("view_recipe", recipe_id=recipe_id))

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    recipe = mongo.db.Recipes.find_one({"_id":ObjectId(recipe_id)})
    categories = mongo.db.Categories.find()
    cuisines = mongo.db.Cuisines.find()
    difficulty = mongo.db.Difficulty.find()
    list_ingredients = '\n'.join(recipe['ingredients'])
    list_allergens = '\n'.join(recipe['allergens'])
    list_instructions = '\n'.join(recipe['instructions'])

    return render_template('edit_recipe.html', recipe=recipe, categories=categories, cuisines=cuisines, difficulty=difficulty, list_ingredients=list_ingredients, list_allergens=list_allergens,list_instructions=list_instructions)

@app.route('/update_recipe/<recipe_id>' , methods=['GET', 'POST'])
def update_recipe(recipe_id):
    recipes = mongo.db.Recipes
    recipe = mongo.db.Recipes.find({"_id":ObjectId(recipe_id)})
    recipes.update({"_id":ObjectId(recipe_id)},{ "$set":
        {
            'recipe_name':request.form['recipe_name'],
            'instructions':string_to_array(request.form['instructions']),
            'serves':request.form['serves'],
            'calories':request.form['calories'],
            'difficulty_level':request.form['difficulty_level'],
            'cooking_time':request.form['cooking_time'],
            'cuisine':request.form['cuisine'],
            'allergens':string_to_array(request.form['allergens']),
            'ingredients':string_to_array(request.form['ingredients']),
            'image_url':request.form['image_url'],
            'category':request.form['category']      
        }})
    return redirect(url_for("view_recipe", recipe_id=recipe_id))

# function to remove a recipe (only the author can remove a recipe)
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.Recipes.remove({"_id":ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))

@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.Categories.remove({"_id":ObjectId(category_id)})
    return redirect(url_for('manage_categories'))

@app.route('/delete_cuisine/<cuisine_id>')
def delete_cuisine(cuisine_id):
    mongo.db.Cuisines.remove({"_id":ObjectId(cuisine_id)})
    return redirect(url_for('manage_categories'))


# function to redirect to the page where the user can add a new category
@app.route('/add_category')
def add_category():
    return render_template('add_category.html')

# function to redirect to the page where the user can add a new cuisine
@app.route('/add_cuisine')
def add_cuisine():
    return render_template('add_cuisine.html')

# function to insert a new category into the database
@app.route('/insert_category', methods=['GET', 'POST'])
def insert_category():
    categories = mongo.db.Categories  
    categories.insert_one({
            'category':request.form['category']
        })
    return redirect(url_for('manage_categories'))

# function to insert a new cuisine into the database
@app.route('/insert_cuisine', methods=['GET', 'POST'])
def insert_cuisine():
    cuisines = mongo.db.Cuisines  
    cuisines.insert_one({
            'cuisine':request.form['cuisine']
        })
    return redirect(url_for('manage_categories'))


# funtion to log out / clear cookie
# https://www.tutorialspoint.com/flask/flask_sessions.htm
@app.route('/logout')
def logout():
 # remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')))
