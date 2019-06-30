import os
import env
from flask import Flask, render_template, request, url_for, redirect, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime



# create an instance of Flask
app = Flask(__name__)

# before deploying convert to enviroment variable
app.config["MONGO_DBNAME"] = 'CookBook'
app.config['MONGO_URI'] = os.environ.get('MONGODB_URI')

# we create an instance of Mongo
mongo = PyMongo(app)

# secret key needed to create session cookies / before deploying convert to enviroment variable
app.secret_key = "randomString123"



# landing page for the website for new users. 
@app.route('/', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session["username"] = request.form["username"]

    # if the cookie for the user already exist the login page is skipped
    if "username" in session:
        return redirect(url_for('get_recipes'))
    
    return render_template('login.html')



#function to get the username at anytime when the user is logged in
def getusername():
    username = session['username']
    return username


def string_to_array(string):
    array = string.split(",")
    return array


@app.route('/get_recipes')
def get_recipes():
    username = getusername()
    return render_template('get_recipes.html', username=username, recipes = mongo.db.Recipes.find())

@app.route('/add_recipe')
def add_recipe():
    categories = mongo.db.Categories.find()
    cuisines = mongo.db.Cuisines.find()
    difficulty = mongo.db.Difficulty.find()
    return render_template('add_recipe.html', categories = categories, cuisines=cuisines, difficulty=difficulty)



@app.route('/insert_recipe', methods=['GET', 'POST'])
def insert_recipe():
    recipes = mongo.db.Recipes  
    recipes.insert_one({
            'recipe_name':request.form['recipe_name'],
            'instructions':string_to_array(request.form['instructions']),
            'serves':request.form['serves'],
            'calories':request.form['calories'],
            'difficulty_level':request.form['difficulty_level'],
            'cooking_time':request.form['cooking_time'],
            'cuisine':request.form['cuisine'],
            'allergens':string_to_array(request.form['allergens']),
            'image_url':request.form['image_url'],
            'author':getusername(),
            'upvotes':0,
            'date':datetime.now(),
            'category':request.form['category']
        })
    recipes.update({'recipe_name':request.form['recipe_name']},{"$push":{"Ingredients":{"ingredient_name":request.form['ingredient_name'],  "amount":request.form['amount']}}})
    return redirect(url_for('get_recipes'))

@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    recipe = mongo.db.Recipes.find_one({"_id":ObjectId(recipe_id)})
    return render_template('view_recipe.html', recipe = recipe)

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.Recipes.remove({"_id":ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))



# https://www.tutorialspoint.com/flask/flask_sessions.htm
@app.route('/logout')
def logout():
 # remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')))
