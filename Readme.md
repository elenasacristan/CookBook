# Time2Eat! – Third milestone project

Time2Eat is an app that allows its users to save their recipes online and edit them anytime they need to. This app also allows the users to share their recipes with other users, vote for the recipes that they like and receive votes from other users.

This app also gives the users the option to search for recipes based on different filters and there is also a section in the website where the user can see some statistics about the recipes and check the ranking of the top rated authors.

See below the link to the website:

http://time2eat-cookbook.herokuapp.com

## UX

This website is targeting people who want to have their recipes stored online and share them with the rest of the world in order to see what other people think of them. Also can be used for people who is only interested on finding recipes to get inspired.

### mock-ups:

Below you can see the mock-ups that I drew using [Pencil](https://pencil.evolus.vn/'https://pencil.evolus.vn/) and [Adobe Fireworks](https://www.adobe.com/products/fireworks.html).

##### Login page

![login](/static/mockups/login_page.jpg)

##### Registration page

![registration](/static/mockups/register_page.jpg)

##### Tips page

![tips](/static/mockups/tips.jpg)

##### Home page

![get_recipes](/static/mockups/get_recipes.jpg)

##### View recipe

![view_recipe](/static/mockups/view_recipe.jpg)

##### Add recipe

![add_recipe](/static/mockups/add_recipe.jpg)

##### Edit recipe

![edit_recipe](/static/mockups/edit_recipe.jpg)

##### Manage Type of meal / cuisines

![manage_categories](/static/mockups/manage_categories.jpg)

##### Statistics

![statistics](/static/mockups/statistics.jpg)

- The final website differs from the original wire-frames because when working on the design sometimes I found nicer ways to display the different sections.

### User stories

- As a user I want to see recipes from other users to get new ideas
- As a user I want to see how many votes each recipe has.
- As a user I want to be able to vote recipes from other users.
- As a user I want to know how many votes my recipes get from other users.
- As a user I want to see the top ranked authors.
- As a user who wants to have access to my recipes from anywhere I want to be able to store my recipes online.
- As a user who wants to update some details from a recipe saved previously I want to be able to edit the recipe.
- As a user who wants organise my recipes I want to be able to remove the recipes that I don't want to keep anymore.
- As a user who wants to add a recipe from a type of meal/cuisine that doesn't exits in the app yet I want to be able to add that type of meal/cuisine to the app.
- As a user who like to keep the app tidy I want to be able to remove types of meal/cuisines that don't have any recipes associated to them.
- As a user who like to get an overall idea of what type of recipes are saved in the app I'd like to see some statistics about the recipes (i.e. recipe charts by difficulty, category, cuisine...)
- As a user who wants to cook a low, medium or high difficulty meal I want to be able to filter the recipes by difficulty.
- As a user who wants to cook a meal from a specific cuisine I want to be able to filter the recipes by cuisines available.
- As a user who wants to make sure the recipes displayed don't contain certain allergens I want to be able to exclude those allergens from the recipes displayed.
- As a user who wants to see a specific type of meal (i.e. breakfast, dinner..) I want to be able to filter by the type of meals available.
- As a user who is not sure how the app works I want to read some instructions to make sure I can take advantage of all the features of the app.
- As a user who is happy with the app I want to follow Time2Eat on social media
- As a user who has experienced any issues with the app or have any questions I want to be able to contact Time2Eat .

## Features

### In all pages

- **Navigation bar:** I have created the navigation bar using [Materialize](<[https://materializecss.com/](https://materializecss.com/)>) nav bar with **Icon Links** and I have also included the **Mobile Collapse Button**. Then I have customised it to be in line with the website design.
- **Tooltips:** I have also added [Materialize](<[https://materializecss.com/](https://materializecss.com/)>) tooltips to give the user additional information about some of the icons in the navigation bar.
- **Mobile Collapse Button / Sidebar:** The **Mobile Collapse Button** will appear in smaller screens (tablets and mobiles) and by clicking on it, it will show the navigation bar as a sidebar.

- **Logo:** The logo will appear in the navigation bar for every section of the website and when clicked it will redirect the user to the home page (get_recipes.html) or to the login page if it is clicked from the "register" page.

- **Social media links:** They appear on the page footer in every page on the website and by clicking on them the user will get re-directed to the media websites to follow Time2Eat. (since the website is fictitious they will be redirected to the login page for facebook or twitter).

- **Sticky Footer:** I have used the sticky footer from [Materialize](<[https://materializecss.com/](https://materializecss.com/)>) to include the social media links and the contact details.
- **Contact Us:** Provides the user with the website contact details in case he/she wants to get in touch.

### login.html

- The login page has an input form where the users will enter their username and password.
- **Flash message** If the username is not registered or if the password is incorrect an error message will appear.
- New users can click on the link "Register here" to get redirected to the register page.

### register.html

- The new users will have to register using the input form in this page in order to start using the app.
- **Flash message** If the username entered in the form has already been used by another user then an error message indicating this issue will be displayed.
- In order to store the passwords securely in MongoDB, the passwords have been hashed using the bcrypt function.

### get_recipes.html

This is the home page where the carousel with all the recipes is displayed. In this page the user can search recipes entering words in the search box and can also filter the recipes using the filter section under the carousel,

- **Search input box**: On the top left corner of the page the users can enter text to search for a specific word in the recipes data base. As a result all the recipes containing that word will be displayed. This can be very useful if you are looking for specific ingredients, name of authors, level of difficulty, cuisine, name of recipe or allergens.

- **Carousel:** The first time the user lands in this page will be able to see all the recipes available in the app by moving sideways using the carousel. The recipes in the carousel will be sorted by number of votes and then by number of views, being the recipe with more votes at the top of the carousel, then if the user moves in the carousel to the right the recipes will be sorted descending by number of votes and number of views and if the user moves to the left then the recipes will be sorted in ascending order.
  By clicking on the image or on the text "view" the user will be redirected to the "view recipe" page where he/she can see all the details available for the recipe.
  At the bottom of the carousel the user can see how many votes and views each recipe has.

- **Filter form**: Below the carousel there is a the filter form. This form is taken from [Materialize](<[https://materializecss.com/](https://materializecss.com/)>) and all the input fields inside the form are also coming from [Materialize](<[https://materializecss.com/](https://materializecss.com/)>). The user will be able to filter the results based on the following criteria:

- **Switch “Only mine”** : The users can activate this switch if they only want to see their own recipes.

- **Select drop-down menu to filter by difficulty:** It will allow the user to filter by difficulty. This filter can be used on its own or as a combination with more filters in the filter section. More than one level of difficulty can be selected.
- **Select dropdown menu to filter by cuisine** : It will allow the user filter by cuisine. This filter can be used on its own or as a combination with more filters in the filter section. More than one cuisine can be selected.
- **Filter by recipes that don't contain certain allergens:** I have added check boxes with the main allergens so the user can select which allergens should be removed from the results.
- **Type of Meal**: The users can tick the check boxes for the type of meal(s) that they are looking recipes for.

### View recipe page

This page will display the main attributes for the recipe. If the recipe belongs to the user he/she will have the options to remove or edit the recipe and if the recipes doesn't belong to the user then the user will have the option to vote for the recipe.

- **Delete button:** This button will only be visible if the recipe belongs to the user and will allow the user to remove the recipe.
  Before the recipe gets removed a confirmation message will appear so the user can confirm if he/she wants to delete the recipe or not.

- **Edit button:** This button will only be visible if the recipe belongs to the user and will allow the user to edit the recipe by redirecting the user to the "edit recipe" page.
- **Vote button:** This button will only be visible if the recipe doesn't belong to the user and by clicking on it the number of votes displayed at the right top of the screen will be incremented by one.
- **Modal:** When the user clicks on "delete button" the confirmation message will be display on a modal window and the recipe will only be removed if "YES" is selected. This modal has been taken from [Materialize](<[https://materializecss.com/](https://materializecss.com/)>).

### add_recipe.html & edit_recipe.html

These pages will be used by the user to enter a new recipe or to edit an existing one.

- **Form:** The whole page is a form with different input types. The form used and all the input fields inside the form have been taken from [Materialize](<[https://materializecss.com/](https://materializecss.com/)>).

- **Input (type text)** I have used input type text for name of the recipe and calories inputs. Name of recipes is required but calories is optional as no everyone may know that information about a recipe. If the calories are not entered then the text 'Not specified' will be used in the Calories section.

- **Modal:** When the user clicks on "Upload image" a modal window will appear containing the input (type file).

- **Input (type file):** Allows the user to upload an image for the recipe. This field is optional. If the user doesn't upload an image then the default image will be used for the recipe.

- **Input (type number):** I have used input type number for the "serves" field. This field will be compulsory.

- **Select input:** I have used "single" select inputs for the fields "Difficulty", "Type of meal" and "Cuisine". All of them are compulsory as they will also be used in the dashboard section and in order to filter the recipes in the home page.
  I have also used "multiple" select input to select the allergens in the recipes. This field won't be required because the recipe may not contain any allergens.

- **Textarea:** I have used textareas for the fields "Instructions" and "Ingredients".
  These fields are compulsory because they are the most important information about any recipe.
  The user needs to enter every ingredient/instruction in a different line to make sure it displays nicely. In order to display it properly I have converted the text to an array separating every ingredient/instruction by "\n".

- **Button 'Add Recipe':** By clicking this button the form will be submitted and the recipe will be inserted into the database.
  After adding the recipe the user gets redirected to the recipe that he/she has just created.

### Manage categories

- **Input box** This input box also comes from [Materialize](<[https://materializecss.com/](https://materializecss.com/)>) and allows the user to enter a new type of meal or cuisine if the type of meal/cuisine that they need is not already on the list displayed below.
- **Flash message** If the type of meal or cuisines entered already exist in the app then a error message will be displayed to let the user know.
- **Table** I'm using a table from [Materialize](<[https://materializecss.com/](https://materializecss.com/)>) in order to display the list of categories and cuisines.
  In the second column of the table the users can see how many recipes there are for each type of meal / cuisine.
- **Remove Type of meal / Cuisine** If a type of meal or cuisine doesn't have any recipes associated then the user will have the option to remove that type of meal / cuisine.

### Tips page

This page is used to explain to the user how to use the app in order to get the most out of it.

- **Material Icons:** I have used material icons matching with the material icons in the nav bar in order to explain the functionality of each part of the website.
  For small screens since the navigation icons disappear from the navigation bar I have also hide the icons for the descriptions of each section.

### Statistics page

This page will give the user an idea of how many and what kind of recipes can be found in the app based on different criteria and also displays a ranking of the top 10 most rated authors.

- **Reset button:** If the users have filtered the charts by clicking on them then they can reset them to the default values by clicking the "Reset" button.

- **Row Chart:** The row charts have been created to display the ranking of the top 10 voted authors and the cuisines available in the app.

- **Pie Chart** They have been used to display the number of recipes split by type of meal and by difficulty.

- **Summary table** The table contains additional information about the recipes filtered and it is sorted descending by number of votes. For each recipe in the table the user can click on the "View" link to get redirected to the recipe page.

## Features Left to Implement

- **Favourites:** I would like to save for each user their favourites recipes so they could save them and access them quicker.
- **Limit the Number of votes:** At the moment the users can vote a recipe more than once but in future I would like to make sure that a user can only vote the same recipe once.
- **Persistence of the filter when searching for recipes** After selecting some filter options and clicking on the filter button I would like to make sure that the options selected on the filters stay selected.

## Technologies Used

#### Database:

- **[MongoDB](<[https://www.mongodb.com/](https://www.mongodb.com/)>)**
  See below the satabase schema:

![database](/static/img/schema.jpg)

#### Mock-up tool:

- **[Pencil:](https://pencil.evolus.vn/'https://pencil.evolus.vn/)** I have used Pencil to create the mock-ups for the website.

#### Graphic Design software:

- **[Adobe Fireworks:](https://www.adobe.com/products/fireworks.html)** I have used Adobe Fireworks to edit the background images, to create the logo and to do some edits on the mock-ups.

#### Languages:

- **HTML5:** Is the main language used to create the structure of the website.

- **CSS3:** Is the language used to add styles to the HTML.

- **[JavaScript:](https://developer.mozilla.org/en-US/docs/Web/JavaScript)** This is the language used to add interactivity to the website. It has been used to create the charts in the statistics page and the funtion to preview the image uploaded using input type file.

- **[Python:](<[https://www.python.org/](https://www.python.org/)>)** The main logic of the website has been created using Python.
- **[Flask:](<[https://palletsprojects.com/p/flask/](https://palletsprojects.com/p/flask/)>)** I have used the web Flask framework.
- **[Jinja:](<[http://jinja.pocoo.org/](http://jinja.pocoo.org/)>)** I have use Jinja templating engine in order to use template inheritance, add for loops and if statements in the html files and in order to pass information between back and frontend.

#### Dependencies:

In order to be able to run my code I had to install the following dependencies:

`from flask import Flask, render_template, request, url_for, redirect, session, flash`

- **render_template** - Used to render html files (they need to be saved on the templates folder)
- **request** - Used to access the form inputs
- **url_for** - Provides a easy way to add urls where needed.
- **redirect** - Used to redirect between views.
- **session** - Needed in order to create a session cookie for the user. That cookie will be removed when the browser is closed or when the user logs out.
- **flash** - Used to send feedback messages to the user.

`from flask_pymongo import PyMongo, DESCENDING`

- **PyMongo** is needed in order to interact with MongoDB
- **DESCENDING** is needed in order to sort the results of the queries in descending order.

`from bson.objectid import ObjectId`

`from bson import json_util`

`from bson.json_util import dumps`

- **bson** (Binary JSON) - MongoDB uses bson so we will need to used the dependency bson in order to convert between BSON and JSON.

`from datetime import datetime`

- **datetime** this dependency will be needed to format the date when a new recipe is added.

`import bcrypt`

- **bcrypt** This dependency will be needed in order to provide a secure login system by hashing the password.

#### Libraries

- **[jQuery](https://jquery.com/)** It is needed for the [Materialize](<[https://materializecss.com/](https://materializecss.com/)>) JavaScript components to function.
- **[D3.js](https://d3js.org/)** JavaScript library is used to create the data visualisations on the "Statistics" page.
- **[DC.js](https://dc-js.github.io/dc.js/)** Is another JavaScript library that provides prebuilt chart types for D3.
- **[Crossfilter.js](http://crossfilter.github.io/crossfilter/)** Is a JavaScript library that allows the charts to be interactive and interdependent of the same dataset.
- **[queue.js](https://github.com/d3/d3-queue)** Is a JavaScript library that is needed in order to wait for the data to be fully loaded before the rest of the code is run.
- **[Material Icons:](<[https://material.io/tools/icons/?style=baseline](https://material.io/tools/icons/?style=baseline)>)** Has been used to add extra meaning on several parts of the website.
- **[FontAwesome:](https://fontawesome.com/ "https://fontawesome.com/")** In some cases if FontAwesome icon was more appropriate I have also used FontAwesome.
- **[Google Fonts:](https://fonts.google.com/ "https://fonts.google.com/")** I’ve used the fonts from Google Fonts to style the fonts in the website.

#### Development environment:

- **[VisualStudio:](https://visualstudio.microsoft.com/)**
  I have used Visual Studio to develop the app.

#### Version control system:

- **[Git:](https://git-scm.com/ "https://git-scm.com/")**
  I have used the version control system Git from the "Git Bash" terminal in order to track changes in the website and push them to GitHub.

#### Hosting service:

- **[Heroku:](<[https://www.heroku.com/](https://www.heroku.com/)>)**
  I have used Heroku in order to deploy the website.

## Testing

### Validation

- **HTML:** I have used https://validator.w3.org/ in order to validate the HTML code.
- **CSS:** I have used https://jigsaw.w3.org/css-validator/ in order to validate the CSS code.
- **JavaScript:** I have used https://jshint.com/ in order to check the JavaScript code.

### Features and responsiveness testing

Click [here](https://github.com/elenasacristan/HolidaysYa/tree/master/assets/Documents/checkList.pdf) to see the checklist that I have used to test all the features in all the screen sizes.

### Additional testing

#### unittest

I have used unittest in order to test the CRUD operations and in order to check that the functions XXXXXXXXXXX works fine.

I have also used development tools in Google Chrome to check how the website would look in different devices (portrait and landscape mode). In addition to that testing I have also asked friends and family to have a look at the website to let me know if everything looks fine on their browsers and devices.

### Problems and bugs:

- \*\*materializa select inputs on some versions of chrome
- **problem2:** fsdfdfsdf

# GitHub repository

1.  I've created a repository in GitHub called: “elenasacristan/CookBook” [https://github.com/elenasacristan/CookBook.git](https://github.com/elenasacristan/CookBook.git)

2.  I've initialised git from the terminal using Git Bash:

    `git init`

3.  I have created a .gitignore file and I have added the files and folder that don't need to be commited (i.e. '.venv' folder)
4.  I've added the files that I was working on to the Staging area by using:

    `git add .`

5.  I've run the commit command with the first commit

    `git commit -m “initial commit"`

6.  I copied from GitHub the following path and I ran it in the Git Bash terminal in order to indicate where my remote repository is:

    `git remote add origin git@github.com:elenasacristan/CookBook.git`

    `git push -u origin master`

7.  After this has been done I've run regular commits after every important update to the code, and I pushed the changes to GitHub.

## Deployment

### Running my code locally

1.  First in vs code I've created a virtual environment:

    `python -m venv .venv`

2.  I've Installed flask

    `python -m pip install flask`

3.  I've created the database in MongoDB Atlas

4.  Then I've installed flask-pymongo for flask to comunicate with mongo:

    `python -m pip install flask-pymongo`

5.  Also in order to be able to use the latest style connection string I've installed dnspython:

        	`python -m pip install dnspython`

6.  Then I've created a env.py file that contains my environmental variables as shown below:
    _where `PASSWORD` and `DATABASE` will contain my password and the name of my database_

        	`import os`

        	`os.environ.setdefault("MONGODB_URI", "mongodb+srv://elenauser:PASSWORD@myfirstcluster-tnijd.mongodb.net/DATABASE?retryWrites=true&w=majority")`

        	`os.environ.setdefault("SECRET_KEY", "RandomString123")`

7.  Then in the app.py I've added `import env` to get the environmental variables that will be needed in the following code:

    `app.config["MONGO_DBNAME"] = 'CookBook'`

    `app.config['MONGO_URI'] = os.environ.get('MONGODB_URI')`

8.  I've have also set the Debug=True ("FLASK_DEBUG": "1") in the vs code settings as shown below:

        `{

    "python.pythonPath": ".venv\\Scripts\\python.exe",
    "python.terminal.activateEnvironment": true,
    "terminal.integrated.env.windows": {
    "FLASK_DEBUG": "1"
    }
    }`

9.  After this I've run the code using the following command:

    `python -m flask run`

### Deployment

I have used Heroku to deploy the website. In order to do that I have followed the steps below:

1. I've changed the settings to Debug=False ("FLASK_DEBUG": "0")
2. I've added the env.py file to the gitignore file.
3. I've removed `import env` from the app.py
4. I've created an app in Heroku
5. In the settings (Config Vars) I've added my environmental variables for the IP, PORT, MONGODB_URI and SECRET_KEY
6. From the command line in vs code I have created a requirements.txt file with the following command:
   `python -m pip freeze > requirements.txt`
7. From the command line in vs code I have created the Procfile with the following command:
   `echo web: python app.py > Procfile`

8. Then I have pushed all the code to my GitHub repository
9. After this **I have linked my Heroku app with my GitHub repository** in order to be able to do "Continous delivery". I've learned how to link Heroku and GitHub with the following tutorial ([https://www.youtube.com/watch?v=\_tiecDrW6yY](https://www.youtube.com/watch?v=_tiecDrW6yY)).
10. Then I have created another app with the same Config Vars and I have created a pipeline where the first app will be the staging app and the second app will be the production app. When I push changes to GitHub I'll be able to see the changes on the Staging App but not in the Production app.
11. Once the website is fully tested and is working correctly the changes done to the statging app will be promoted to the Production app:
    [https://time2eat-cookbook.herokuapp.com/](https://time2eat-cookbook.herokuapp.com/)

### My repository

https://github.comelenasacristan/CookBook/

### My deployed app

http://time2eat-cookbook.herokuapp.com

## Credits

#### Content

- **Data:** The data for the recipes has been collected from https://en.wikibooks.org/wiki/Category:Recipes

#### Media

##### background image login / register page

- The image used for the background image in the intro page was obtained from Google images using the Advance Search and selecting “free to use, share or modify, even commercially”. See link below:

      	[https://www.maxpixel.net/Frying-Pan-Cooking-Food-Cook-Figure-Fried-3125716](https://www.maxpixel.net/Frying-Pan-Cooking-Food-Cook-Figure-Fried-3125716)

##### recipes images

- The recipes images have been obtained from Google images using the Advance Search and selecting “free to use, share or modify, even commercially”. See links below:

      	[https://www.seriouseats.com/2015/05/pancakes-around-the-world.html](https://www.seriouseats.com/2015/05/pancakes-around-the-world.html)

      	[https://pixabay.com/photos/food-fish-chips-fish-and-chips-3687804/](https://pixabay.com/photos/food-fish-chips-fish-and-chips-3687804/)

      	[https://pixabay.com/images/search/burger/](https://pixabay.com/images/search/burger/)

      	[https://commons.wikimedia.org/wiki/File:Bolo_de_Mel.JPG](https://commons.wikimedia.org/wiki/File:Bolo_de_Mel.JPG)

      	[https://www.flickr.com/photos/30478819@N08/35961379924](https://www.flickr.com/photos/30478819@N08/35961379924)

      	[https://www.flickr.com/photos/146966953@N02/28879437404](https://www.flickr.com/photos/146966953@N02/28879437404)

      	[https://www.flickr.com/photos/39908901@N06/8406293769](https://www.flickr.com/photos/39908901@N06/8406293769)

      	[https://www.flickr.com/photos/jeffreyww/5063817774](https://www.flickr.com/photos/jeffreyww/5063817774)

      	[https://www.flickr.com/photos/ellaolsson/30863436677](https://www.flickr.com/photos/ellaolsson/30863436677)

      	[https://pxhere.com/en/photo/619505](https://pxhere.com/en/photo/619505)

      	[https://pixabay.com/photos/iced-coffee-coffee-drink-2710815/](https://pixabay.com/photos/iced-coffee-coffee-drink-2710815/)

      	[https://www.flickr.com/photos/30478819@N08/43801037610](https://www.flickr.com/photos/30478819@N08/43801037610)

      	[https://pixabay.com/photos/salad-tuna-salad-article-nafut-1088411/](https://pixabay.com/photos/salad-tuna-salad-article-nafut-1088411/)

## Acknowledgements

**Templates**

- I have used the following bootstrap login design to help me creating the login/register pages and then I have modified the colours and image.

[https://startbootstrap.com/snippets/sign-in-split/](https://startbootstrap.com/snippets/sign-in-split/)

**Tutorials**

- **Login / Register**:
  I watch the following tutorial to understand how to create the login/register functions.
  [https://www.youtube.com/watch?v=vVx1737auSE](https://www.youtube.com/watch?v=vVx1737auSE)

- **Upload image**
  I found information about how to upload images into mongodb using flask on the following video tutorial:
  [https://www.youtube.com/watch?v=DsgAuceHha4](https://www.youtube.com/watch?v=DsgAuceHha4)

- **Display image as soon as it is selected**
  The following post help me to create the code in order to display the image as soon as it is selected using the input file.
  [https://gist.github.com/zulhfreelancer/1a1b68062da349d6268f0aaa43991b99](https://gist.github.com/zulhfreelancer/1a1b68062da349d6268f0aaa43991b99)

- **Create interactive visualization using DC/JS Crossfilter**
  I learn how to set up the connection between mongodb and DC/JS Crossfilter by following the tutorial in the link below:
  http://adilmoujahid.com/posts/2015/01/interactive-data-visualization-d3-dc-python-mongodb/

- **Log out / clear cookies**
  In the link below I learnt about how to remove the cookies when the user logs out. https://www.tutorialspoint.com/flask/flask_sessions.htm
- As always the slack community has been very helpful when I had any question.
- I'm also really thankful to the Tutors who help me understanding how to set up environmental variables in vscode.
  <!--stackedit_data:
  eyJoaXN0b3J5IjpbOTAyMjA3MDAsLTg5MzA0MzMxMiwxNTgzMD
  kzMTE0LDE4NDE3Mzc4NTMsMzQ1NDQ3MTkzLC0xODczMDc3MzM3
  XX0=
  -->
