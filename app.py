import os
# env is where I have my environmental variables and it is only used for to run my code locally
import env
import json
from flask import Flask, render_template, request, url_for, redirect, session
from flask_pymongo import PyMongo, DESCENDING
from bson.objectid import ObjectId
from bson import json_util
from bson.json_util import dumps
from datetime import datetime
import bcrypt


# create an instance of Flask
app = Flask(__name__)


# before deploying convert to enviroment variable
app.config["MONGO_DBNAME"] = 'CookBook'
app.config['MONGO_URI'] = os.environ.get('MONGODB_URI')


# we create an instance of Mongo
mongo = PyMongo(app)


# secret key needed to create session cookies
app.secret_key = os.environ.get('SECRET_KEY')


#function use to convert strings separated by commas to arrays
def string_to_array(string):
    array = string.split("\n")
    return array
    

# landing page for the website for new users. I learn how to create the login/register functionality by watchin this tutorial https://www.youtube.com/watch?v=vVx1737auSE
@app.route('/')
def index():
   
    # if the cookie for the user already exist the login page is skipped
    if "username" in session:
        return redirect(url_for('get_recipes'))
    
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.Users
    user_login = users.find_one({'author':request.form['username'].capitalize()})

    if user_login:
        if bcrypt.hashpw(request.form['password'].encode('utf-8'), user_login['password']) == user_login['password']:
            session["username"] = request.form["username"].capitalize()
            return redirect(url_for('get_recipes'))
    
    message = 'The login details are not correct'
    return render_template('login.html', message=message)


@app.route('/register', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.Users
        user_exists = users.find_one({'author':request.form['username'].capitalize()})

        if user_exists is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'author':request.form['username'].capitalize(), 'password':hashpass})
            session['username'] = request.form['username'].capitalize()
            return redirect(url_for('get_recipes'))

        message = "That username already exists, please choose a different one."
        return render_template('register.html', message=message)

    return render_template('register.html')


#home page, the recipes are sorted by votes and views. The most voted will be on the top one of the carousel and the it will be in descending order if you move to the right
@app.route('/get_recipes')
def get_recipes():
    title = "View recipes"
    username = session['username']
    recipes = mongo.db.Recipes.find().sort([("upvotes",DESCENDING), ("views",DESCENDING)])
    recipes_count = recipes.count()
    allergens = mongo.db.Allergens.find()
    categories = mongo.db.Categories.find()
    cuisines = mongo.db.Cuisines.find()
    difficulty = mongo.db.Difficulty.find()
    return render_template('get_recipes.html', title=title, username=username, recipes = recipes, categories = categories, cuisines=cuisines, difficulty=difficulty, allergens=allergens, recipes_count=recipes_count)


@app.route('/search', methods=['GET', 'POST'])
def search():
    title = "View recipes"
    username = session['username']
    allergens = mongo.db.Allergens.find()
    categories = mongo.db.Categories.find()
    cuisines = mongo.db.Cuisines.find()
    difficulty = mongo.db.Difficulty.find()
    recipes = mongo.db.Recipes.find()

    '''GET THE WORD/SENTENCE FROM THE SEARCH BOX'''    
    text_to_find = request.form["text_to_find"]

    '''CREATE TEXT INDEX FOR ALL TEXT FIELDS'''    
    mongo.db.Recipes.create_index( [("$**", 'text')] )

    '''Search result sorted by upvotes and after sorted by number of views'''    
    recipes = mongo.db.Recipes.find({ "$text": { "$search": text_to_find } }).sort([("upvotes",DESCENDING), ("views",DESCENDING)])
    recipes_count = recipes.count()
        
    # send recipes to page
    return render_template('get_recipes.html', title=title, username=username, recipes = recipes, categories = categories, cuisines=cuisines, difficulty=difficulty, allergens=allergens, recipes_count=recipes_count)
    
    
@app.route('/filter_recipes', methods = ['GET', 'POST'])
def filter_recipes():
    title = "View recipes"
    username = session['username']
    allergens = mongo.db.Allergens.find()
    categories = mongo.db.Categories.find()
    cuisines = mongo.db.Cuisines.find()
    difficulty = mongo.db.Difficulty.find()
    recipes = mongo.db.Recipes.find()
    
    #create different query depending on if a cuisine has been selected or not in the dropdown menu
    if request.form.getlist('cuisine') != []:
        query_cuisine = {"cuisine":{ "$in": request.form.getlist('cuisine')}}
    else:
        query_cuisine = {"cuisine":{ "$in": recipes.distinct('cuisine')}}
    
    #create different query depending on if a difficulty has been selected or not in the dropdown menu
    if request.form.getlist('difficulty') != []:
        query_difficulty = {"difficulty":{ "$in": request.form.getlist('difficulty')}}
    else:
        query_difficulty = {"difficulty":{ "$in": recipes.distinct('difficulty')}}

    # from the checkboxes in the filter section get the list of allergens to exclude 
    allergens_to_remove = request.form.getlist('allergens')
    
    #show all the recipes that DON'T contain the allergens selected
    query_allergens = {"allergens": { "$nin": allergens_to_remove } }

    # from the checkboxes in the filter section get the list of categories to display 
    categories_to_display = request.form.getlist('categories')
    
    # create different query depending on if there categories are checked or not
    if categories_to_display == []:
        query_categories = {"category": { "$in": recipes.distinct('category') } }
    else:
        query_categories = {"category": { "$in": request.form.getlist('categories') } }
    
    # create different query depending is the user selects "only_mine" or not"
    if request.form.get('only_mine') == 'only_mine':
        query_author = {"author": username }
    else:
        query_author = {"author": { "$in": recipes.distinct('author') } }
        
    recipes = mongo.db.Recipes.find({"$and":[query_author,query_difficulty,query_cuisine,query_allergens, query_categories]}).sort([("upvotes",DESCENDING), ("views",DESCENDING)])
    recipes_count = recipes.count()

    return render_template('get_recipes.html', title=title, username=username, recipes = recipes, categories = categories, cuisines=cuisines, difficulty=difficulty, allergens=allergens, recipes_count=recipes_count)


#route to the tips page
@app.route('/tips')
def tips():
    return render_template('tips.html')


# function to add new recipe
@app.route('/add_recipe')
def add_recipe():
    title = "Add recipe"
    allergens = mongo.db.Allergens.find()
    categories = mongo.db.Categories.find()
    cuisines = mongo.db.Cuisines.find()
    difficulty = mongo.db.Difficulty.find()
    return render_template('add_recipe.html', title=title, categories = categories, cuisines=cuisines, difficulty=difficulty, allergens=allergens)


# function to see and insert new categories or cuisines
@app.route('/manage_categories')
def manage_categories():
    title = "Manage categories / cuisines"
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

    return render_template('manage_categories.html', title=title, categories = category_object, cuisines = cuisine_object)


# funtion to insert into the database the new recipe
@app.route('/insert_recipe', methods=['GET', 'POST'])
def insert_recipe():
    '''https://www.youtube.com/watch?v=DsgAuceHha4'''
    if 'recipe_image' in request.files:
        recipe_image = request.files['recipe_image']
        if recipe_image != "":
            mongo.save_file(recipe_image.filename, recipe_image)
        if request.form['calories']:
            calories = request.form['calories']
        else:
            calories = "Not specified"

        mongo.db.Recipes.insert({
                'recipe_name':request.form['recipe_name'].capitalize(),
                'instructions':string_to_array(request.form['instructions']),
                'serves':request.form['serves'],
                'calories':calories,
                'difficulty':request.form['difficulty'],
                'cooking_time':request.form['cooking_time'],
                'cuisine':request.form['cuisine'],
                'allergens':request.form.getlist('allergens'),
                'ingredients':string_to_array(request.form['ingredients']),
                'recipe_image':recipe_image.filename,
                'author':session['username'],
                'upvotes':0,
                'date':datetime.now().strftime("%d/%m/%Y"),
                'category':request.form['category']
            })
    return redirect(url_for('get_recipes'))


@app.route('/img_uploads/<filename>')
def img_uploads(filename):
    return mongo.send_file(filename)


# function to see a recipe after clicking on its image or "view" link
@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    mongo.db.Recipes.update_one({"_id":ObjectId(recipe_id)}, {'$inc': {'views': 1}})
    recipe = mongo.db.Recipes.find_one({"_id":ObjectId(recipe_id)})

    return render_template('view_recipe.html', recipe = recipe, username = session['username'])


# function to vote the recipes (the recipe author is not allowed to vote)
@app.route('/view_recipe/vote/<recipe_id>')
def vote(recipe_id):
    mongo.db.Recipes.update_one({"_id":ObjectId(recipe_id)}, {'$inc': {'upvotes': 1}})
    return redirect(url_for("view_recipe", recipe_id=recipe_id))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    recipe = mongo.db.Recipes.find_one({"_id":ObjectId(recipe_id)})
    allergens = mongo.db.Allergens.find()
    categories = mongo.db.Categories.find()
    cuisines = mongo.db.Cuisines.find()
    difficulty = mongo.db.Difficulty.find()
    list_ingredients = '\n'.join(recipe['ingredients'])
    list_allergens = '\n'.join(recipe['allergens'])
    list_instructions = '\n'.join(recipe['instructions'])

    return render_template('edit_recipe.html', recipe=recipe, categories=categories, cuisines=cuisines, difficulty=difficulty, list_ingredients=list_ingredients, list_allergens=list_allergens,list_instructions=list_instructions, allergens=allergens)


@app.route('/update_recipe/<recipe_id>' , methods=['GET', 'POST'])
def update_recipe(recipe_id):
    recipes = mongo.db.Recipes
    recipe = mongo.db.Recipes.find({"_id":ObjectId(recipe_id)})
    if 'recipe_image' in request.files:
            recipe_image = request.files['recipe_image']
            mongo.save_file(recipe_image.filename, recipe_image)

            recipes.update({"_id":ObjectId(recipe_id)},{ "$set":
                {
                    'recipe_name':request.form['recipe_name'].capitalize(),
                    'instructions':string_to_array(request.form['instructions']),
                    'serves':request.form['serves'],
                    'calories':request.form['calories'],
                    'difficulty':request.form['difficulty'],
                    'cooking_time':request.form['cooking_time'],
                    'cuisine':request.form['cuisine'],
                    'allergens':request.form.getlist('allergens'),
                    'ingredients':string_to_array(request.form['ingredients']),
                    'category':request.form['category']      
                }})

            if recipe_image.filename != "":   
                recipes.update({"_id":ObjectId(recipe_id)},{ "$set":
                {
                    'recipe_image':recipe_image.filename,
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
            'category':request.form['category'].capitalize()
        })
    return redirect(url_for('manage_categories'))


# function to insert a new cuisine into the database
@app.route('/insert_cuisine', methods=['GET', 'POST'])
def insert_cuisine():
    cuisines = mongo.db.Cuisines  
    cuisines.insert_one({
            'cuisine':request.form['cuisine'].capitalize()
        })
    return redirect(url_for('manage_categories'))


# http://adilmoujahid.com/posts/2015/01/interactive-data-visualization-d3-dc-python-mongodb/
# we use this route to retrieve all the recipes from the database in json format
@app.route("/data_recipes")
def data():
    recipes = mongo.db.Recipes.find(projection = {'_id':True ,'recipe_name': True, 'upvotes': True,'category': True, 'difficulty': True, 'cuisine': True, 'author':True})
    json_recipes = []

    for recipe in recipes:
        json_recipes.append(recipe)
    json_recipes = json.dumps(json_recipes, default=json_util.default, indent= 4, sort_keys=True)
         
    return json_recipes
    

@app.route("/statistics")
def statistics():
    return render_template('statistics.html')


# funtion to log out / clear cookie
# https://www.tutorialspoint.com/flask/flask_sessions.htm
@app.route('/logout')
def logout():
 # remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('index'))



'''
This code below has been used in order to create a backup of my database
'''

'''
def back_up_collection(collection, path):
    json_array = []

    for document in collection:
        json_array.append(document)
    json_array = json.dumps(json_array, default=json_util.default, indent= 4, sort_keys=True)

    f = open(path,"w")
    f.write(json_array)
    f.close()

@app.route("/data_backup")
def data_backup():
    recipes = mongo.db.Recipes.find()
    allergens = mongo.db.Allergens.find()
    categories = mongo.db.Categories.find()
    cuisines = mongo.db.Cuisines.find()
    difficulty = mongo.db.Difficulty.find()
    users = mongo.db.Users.find()
    chucks = mongo.db.fs.chunks.find()
    files = mongo.db.fs.files.find()
   
    back_up_collection(recipes, "static/collections_backup/json_recipes_bk.json")
    back_up_collection(allergens, "static/collections_backup/json_allergens_bk.json")
    back_up_collection(categories, "static/collections_backup/json_categories_bk.json")
    back_up_collection(cuisines, "static/collections_backup/json_cuisines_bk.json")
    back_up_collection(difficulty, "static/collections_backup/json_difficulty_bk.json")
    back_up_collection(users, "static/collections_backup/json_users_bk.json")
    back_up_collection(chucks, "static/collections_backup/json_chucks_bk.json")
    back_up_collection(files, "static/collections_backup/json_files_bk.json")

    return 'Done'
'''


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')))
