
import unittest
import env
import os
from mockupdb import MockupDB, go, Command
from pymongo import MongoClient
from bson import ObjectId as mockup_oid
from json import dumps
from pymongo import MongoClient

from app import string_to_array, app

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
        data = {"name":"chocolate", "cooking_time":"3 days"}
        self.recipes_coll.insert_one(data)
        number_recipes = self.recipes_coll.find().count()
        self.assertEqual(number_recipes,1)
    
    # tests read
    def test_read_recipe(self):
        self.recipes_coll.remove()
        data = [{"name":"chocolate", "cooking_time":"3 days"},{"name":"cereals", "cooking_time":"2 days"},{"name":"bread", "cooking_time":"1 days"}]
        self.recipes_coll.insert(data)
        number_recipes = self.recipes_coll.find().count()
        self.assertEqual(number_recipes,3)
    
    def test_read_recipe2(self):
        self.recipes_coll.remove()
        data = [{"name":"chocolate", "cooking_time":"3 days"},{"name":"cereals", "cooking_time":"2 days"},{"name":"bread", "cooking_time":"1 days"}]
        self.recipes_coll.insert(data)
        number_recipes = self.recipes_coll.find().count()
        self.assertNotEqual(number_recipes,0)

    # tests update
    def test_update_recipe(self):
        self.recipes_coll.remove()
        data = {"name":"chocolate", "cooking_time":"3 days"}
        self.recipes_coll.insert_one(data)
        self.recipes_coll.update_one({"name":"chocolate"},{'$set':{"name":"milk"}})
        name = self.recipes_coll.find_one({"name":"milk"})
        self.assertEqual(name['name'],"milk")
    
    def test_update_recipe2(self):
        self.recipes_coll.remove()
        data = {"name":"chocolate", "cooking_time":"3 days"}
        self.recipes_coll.insert_one(data)
        self.recipes_coll.update_one({"name":"chocolate"},{'$set':{"name":"milk"}})
        name = self.recipes_coll.find_one({"name":"milk"})
        self.assertNotEqual(name['name'],"chocolate")

    #tests delete   
    def test_remove_cuisine(self):
        data = {"cuisine":"Indian"}
        self.cuisines_coll.insert_one(data)
        self.cuisines_coll.remove({"cuisine":"Indian"})
        num_cuisines = self.cuisines_coll.find().count()
        self.assertEqual(num_cuisines,0)

    def test_remove_cuisine1(self):
        data = {"cuisine":"Indian"}
        self.cuisines_coll.insert_one(data)
        self.cuisines_coll.remove({"cuisine":"Indian"})
        num_cuisines = self.cuisines_coll.find().count()
        self.assertNotEqual(num_cuisines,1)

    # test search
    def test_search(self):
        self.recipes_coll.remove()
        data = [{"name":"chocolate", "cooking_time":"3 days"},{"name":"chocolate", "cooking_time":"3 days"},{"name":"cereals", "cooking_time":"2 days"},{"name":"bread", "cooking_time":"1 days"}]
        self.recipes_coll.insert(data)
        self.recipes_coll.create_index( [("$**", 'text')])
        recipes = self.recipes_coll.find({ "$text": { "$search": "chocolate" } })
        count = recipes.count()
        self.assertEqual(count,2)

    ############# test filter  CONTINUE
    def test_filter(self):
        self.recipes_coll.remove()
        data = [{"name":"chocolate", "allergen":"3 days"},{"name":"chocolate", "cooking_time":"3 days"},{"name":"cereals", "cooking_time":"2 days"},{"name":"bread", "cooking_time":"1 days"}]
        self.recipes_coll.insert(data)
        allergens = {"allergens": { "$nin": allergens_to_remove } }
        count = allergens.count()
        self.assertEqual(count,2)

if __name__ == '__main__':
    unittest.main()