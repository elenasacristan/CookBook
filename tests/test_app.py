# The followin lines of code were created with help from my mentor: line 2-9, and 153-180. And from 180 it was created by myself
import unittest
import env
import os
from mockupdb import MockupDB, go, Command
from pymongo import MongoClient
from bson import ObjectId as mockup_oid
from json import dumps
from pymongo import MongoClient

from main import string_to_array, app
recipe = {
        "recipe_name": "Rice pudding",
        "allergens": ["Eggs", "Milk", "Tree nuts"],
        "author": "Juan",
        "calories": "98",
        "category": "Dessert",
        "cooking_time": "2 hours",
        "cuisine": "International",
        "date": "04/07/2019",
        "difficulty": "Medium",
        "ingredients": [
            "milk\r",
            "eggs\r",
            "sugar\r",
            "rice\r",
        ],
        "instructions": [
            "Preheat.\r",
            "Mix\r",
            "Place\r",
            "Bake.\r"
        ],
        "recipe_image": "ricepudding.jpg",    
        "serves": 2,
        "upvotes": 2,
        "views": 8}

datafilter = [{"recipe_image": "jerkchicken.jpg",
        "allergens": ["Mustard"],
        "author": "John",
        "calories": "500",
        "category": "Dinner",
        "cooking_time": "1h 10min",
        "cuisine": "Jamaican",
        "date": "03/07/2019",
        "difficulty": "Medium",
        "ingredients": [
            "all spice\r",
            "salt\r",
            "dehydrated lemon peel\r",
            "dark rum\r",
            "chicken breasts\r",
            "mustard"
        ],
        "instructions": [
            "Combine\r",
            "Place\r",
            "Turn"
        ],
        "recipe_image": "jerkchicken.jpg",
        "serves": 4,
        "upvotes": 3,
        "views": 10
    },
    {
	"recipe_name": "Pancakes",
        "allergens": ["Gluten"],
        "author": "Elena",
        "calories": "227",
        "category": "Breakfast",
        "cooking_time": "30 min",
        "cuisine": "American",
        "date": "04/07/2019",
        "difficulty": "Low",
        "ingredients": [
            "flour\r",
            "salt\r",
            "milk\r",
            "egg\r",
            "sugar"
        ],
        "instructions": [
            "Mix\r",
            "Add.\r",
            "Separate.\r",
            "Beat whites.\r"
            
        ],
        "recipe_image": "pancakes.jpg",
        "serves": 4,
        "upvotes": 1,
        "views": 1
    },
    {
	"recipe_name": "Beef stroganoff",
        "allergens": ["Mustard"],
        "author": "Maria",
        "calories": "98",
        "category": "Dinner",
        "cooking_time": "45 min",
        "cuisine": "Russian",
        "date": "04/07/2019",
        "difficulty": "High",
        "ingredients": [
            "salt\r",
            "black pepper\r",
            "butter\r",
            "green onions\r"        
        ],
        "instructions": [
            "Remove any fat.\r",
            "Melt\r",
            "Stir\r",
            "Cover.\r",
            "Heat."
        ],
        "recipe_image": "BeefStroganoff.jpg",    
        "serves": 2,
        "upvotes": 2,
        "views": 8
    },
{
	"recipe_name": "Rice pudding",
        "allergens": ["Eggs", "Milk", "Tree nuts"],
        "author": "Juan",
        "calories": "98",
        "category": "Dessert",
        "cooking_time": "2 hours",
        "cuisine": "International",
        "date": "04/07/2019",
        "difficulty": "Medium",
        "ingredients": [
            "milk\r",
            "eggs\r",
            "sugar\r",
            "rice\r",
           
        ],
        "instructions": [
            "Preheat.\r",
            "Mix\r",
            "Place\r",
            "Bake.\r"
        ],
        "recipe_image": "ricepudding.jpg",    
        "serves": 2,
        "upvotes": 2,
        "views": 8}]


class TestApp(unittest.TestCase):
    @classmethod
    def setUpClass(self):
             
        # create mongo connection to mock server
        app.testing = True
        self.mongo_client=MongoClient(os.environ.get('TEST_MONGODB_URI'))
        self.app = app.test_client()
        self.db = self.mongo_client['test_CookBook']
        self.recipes_coll = self.db['recipes']
        self.cuisines_coll = self.db['cuisines']
        self.allergens_coll = self.db['allergens']

    @classmethod
    def tearDownClass(self):
        self.mongo_client.drop_database('test_CookBook')
    
# test string_to_array funcion operations
    def test_string_to_array(self):
        self.assertEqual(string_to_array("1\n2\n3"), ["1","2","3"])

# test CRUD operations           
    # test create
    def test_insert_recipe(self):
        self.recipes_coll.remove()
        self.recipes_coll.insert_one(recipe)
        number_recipes = self.recipes_coll.find().count()
        self.assertEqual(number_recipes,1)

# From here the rest of the code was created by myself
    # tests read
    def test_read_recipe(self):
        self.recipes_coll.remove()
        self.recipes_coll.insert(datafilter)
        number_recipes = self.recipes_coll.find().count()
        self.assertEqual(number_recipes,4)
    
    def test_read_recipe2(self):
        self.recipes_coll.remove()
        self.recipes_coll.insert(datafilter)
        number_recipes = self.recipes_coll.find().count()
        self.assertNotEqual(number_recipes,0)

    # tests update
    def test_update_recipe(self):
        self.recipes_coll.remove()
        self.recipes_coll.insert_one(recipe)
        self.recipes_coll.update_one({"author":"Juan"},{'$set':{"author":"Carlos"}})
        author = self.recipes_coll.find_one({"author":"Carlos"})
        self.assertEqual(author['author'],"Carlos")
    
    def test_update_recipe2(self):
        self.recipes_coll.remove()
        self.recipes_coll.insert_one(recipe)
        self.recipes_coll.update_one({"author":"Juan"},{'$set':{"author":"Carlos"}})
        author = self.recipes_coll.find_one({"author":"Carlos"})
        self.assertNotEqual(author['author'],"Juan")

    #tests delete   
    def test_remove_cuisine(self):
        cuisines = [{"cuisine":"International"},{"cuisine":"Indian"},{"cuisine":"Spanish"}]
        self.cuisines_coll.insert(cuisines)
        self.cuisines_coll.remove({"cuisine":"Indian"})
        num_cuisines = self.cuisines_coll.find().count()
        self.assertEqual(num_cuisines,2)

    def test_remove_cuisine1(self):
        cuisines = [{"cuisine":"International"},{"cuisine":"Indian"},{"cuisine":"Spanish"}]
        self.cuisines_coll.insert(cuisines)
        self.cuisines_coll.remove({"cuisine":"Indian"})
        num_cuisines = self.cuisines_coll.find().count()
        self.assertNotEqual(num_cuisines,3)

    # test search
    def test_search(self):
        self.recipes_coll.remove()
        self.recipes_coll.insert(datafilter)
        self.recipes_coll.create_index( [("$**", 'text')])
        recipes = self.recipes_coll.find({ "$text": { "$search": "salt" } })
        count = recipes.count()
        self.assertEqual(count,3)


    #tests filters
    def test_filter_allergens(self):
        self.recipes_coll.remove()
        self.recipes_coll.insert(datafilter)

        allergens_to_remove = ["Gluten","Eggs"]
        query_allergens = {"allergens": { "$nin": allergens_to_remove }}
        
        recipes = self.recipes_coll.find(query_allergens)
        count = recipes.count()
        
        self.assertEqual(count,2)


    def test_filter_allergens2(self):
        self.recipes_coll.remove()
        self.recipes_coll.insert(datafilter)
        
        allergens_to_remove = []
        query_allergens = {"allergens": { "$nin": allergens_to_remove }}
        
        recipes = self.recipes_coll.find(query_allergens)
        count = recipes.count()
        
        self.assertEqual(count,4)


    def test_filter_difficulty(self):
        
        self.recipes_coll.remove()
        self.recipes_coll.insert(datafilter)

        difficulty_selected_in_form = ["High"]

        if difficulty_selected_in_form  != []:
            query_difficulty = {'difficulty':{ "$in": difficulty_selected_in_form }}
        else:
            query_difficulty = {'difficulty':{ "$in": self.recipes_coll.distinct('difficulty')}}

        recipes = self.recipes_coll.find(query_difficulty)    
        count = recipes.count()   
        
        self.assertEqual(count,1)


    def test_filter_difficulty2(self):
        
        self.recipes_coll.remove()
        self.recipes_coll.insert(datafilter)

        difficulty_selected_in_form = []

        if difficulty_selected_in_form  != []:
            query_difficulty = {'difficulty':{ "$in": difficulty_selected_in_form }}
        else:
            query_difficulty = {'difficulty':{ "$in": self.recipes_coll.distinct('difficulty')}}

        recipes = self.recipes_coll.find(query_difficulty) 
        count = recipes.count()
            
        self.assertEqual(count,4)


    def test_filter_cuisine(self):
        
        self.recipes_coll.remove()
        self.recipes_coll.insert(datafilter)

        cuisine_selected_in_form = ["International","Russian","Jamaican"]

        if cuisine_selected_in_form  != []:
            query_cuisine = {'cuisine':{ "$in": cuisine_selected_in_form }}
        else:
            query_cuisine = {'cuisine':{ "$in": self.recipes_coll.distinct('cuisine')}}

        recipes = self.recipes_coll.find(query_cuisine) 
        count = recipes.count()
            
        self.assertEqual(count,3)


    def test_filter_cuisine2(self):
        
        self.recipes_coll.remove()
        self.recipes_coll.insert(datafilter)

        cuisine_selected_in_form = []

        if cuisine_selected_in_form != []:
            query_cuisine = {'cuisine':{ "$in": cuisine_selected_in_form }}
        else:
            query_cuisine = {'cuisine':{ "$in": self.recipes_coll.distinct('cuisine')}}

        recipes = self.recipes_coll.find(query_cuisine) 
        count = recipes.count()
            
        self.assertEqual(count,4)



    def test_filter_category(self):
        
        self.recipes_coll.remove()
        self.recipes_coll.insert(datafilter)

        category_selected_in_form = ["Dinner"]

        if category_selected_in_form != []:
            query_category = {'category':{ "$in": category_selected_in_form }}
        else:
            query_category = {'category':{ "$in": self.recipes_coll.distinct('category')}}

        recipes = self.recipes_coll.find(query_category) 
        count = recipes.count()
            
        self.assertEqual(count,2)


    def test_filter_category2(self):
        
        self.recipes_coll.remove()
        self.recipes_coll.insert(datafilter)

        category_selected_in_form = []

        if category_selected_in_form != []:
            query_category = {'category':{ "$in": category_selected_in_form }}
        else:
            query_category = {'category':{ "$in": self.recipes_coll.distinct('category')}}

        recipes = self.recipes_coll.find(query_category) 
        count = recipes.count()
            
        self.assertEqual(count,4)


    def test_more_than_one_filter(self):

        self.recipes_coll.remove()
        self.recipes_coll.insert(datafilter)

        allergens_to_remove = ["Milk"]
        difficulty_selected_in_form = ["Medium"]

        query_allergens = {"allergens": { "$nin": allergens_to_remove }}

        if difficulty_selected_in_form  != []:
            query_difficulty = {'difficulty':{ "$in": difficulty_selected_in_form }}
        else:
            query_difficulty = {'difficulty':{ "$in": self.recipes_coll.distinct('difficulty')}}

        recipes = self.recipes_coll.find({"$and":[query_allergens,query_difficulty]})
        recipes_count = recipes.count()
            
        self.assertEqual(recipes_count,1)


if __name__ == '__main__':
    unittest.main()