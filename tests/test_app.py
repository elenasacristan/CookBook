
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
        data = {"name":"chocolate", "serves":"3 days"}
        self.recipes_coll.insert_one(data)
        number_recipes = self.recipes_coll.find().count()
        self.assertEqual(number_recipes,1)

    # test read
    def test_read_recipe(self):
        all_recipes = self.recipes_coll.find()
        self.assertTrue(all_recipes)

    # test update
    def test_update_recipe(self):
        data = {"name":"chocolate", "serves":"3 days"}
        self.recipes_coll.insert_one(data)
        self.recipes_coll.update_one({"name":"chocolate"},{'$set':{"name":"milk"}})
        name = self.recipes_coll.find_one({"name":"milk"})
        self.assertEqual(name['name'],"milk")

    #test delete   
    def test_remove_cuisine(self):
        data = {"cuisine":"Indian"}
        self.cuisines_coll.insert_one(data)
        self.cuisines_coll.remove({"cuisine":"Indian"})
        num_cuisines = self.cuisines_coll.find().count()
        self.assertEqual(num_cuisines,0)
    
    
if __name__ == '__main__':
    unittest.main()