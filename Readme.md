# Time2Eat! – Third milestone project

Time2Eat is an app that allows its users to save their recipes online and edit them anytime they need to. This app also allows the users to share their recipes with other users, vote for the recipes that they like and recieve votes from other users.

This app also gives the users the option to search for recipes based on different filters and there is also a section in the website where the user can see some statistics about the recipes and check the ranking of the top rated authors.

See below the link to the website:

[https://elenasacristan.github.io/Cookbook/](https://elenasacristan.github.io/Cookbook/)

## UX

This website is targeting people who want to have their recipes stored online and share them with the rest of the world in order to see what other people think of them. Also can be used for people who is only interested on finding recipes to get inspired.

### mock-ups:

Below you can see the mock-ups that I drew using Pencil:

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

- The final website differs from the original wireframes because when working on the design sometimes I found nicer ways to display the different sections.

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
- As a user who like to keep the app tidy I want to be able to remove categories/cuisines that don't have any recipes associated to them.
- As a user who like to get an overall idea of what type of recipes are saved in the app I'd like to see some statistics about the recipes (i.e. recipe charts by difficulty, category, cuisine...)
- As a user who wants to cook a low, medium or high difficulty meal I want to be able to filter the recipes by difficulty.
- As a user who wants to cook a meal from a specific cuisine I want to be able to filter the recipes by cuisines available.
- As a user who wants to make sure the recipes displayed don't contain certain allergens I want to be able to exclude those allergens from recipes displayed.
- As a user who wants to see a specific type of meal (i.e. breakfast, dinner..) I want to be able to filter by the type of meals available.
- As a user who is not sure how the app works I want to read some instructions to make sure I can take advantage of all the features of the app.
- As a user who is happy with the app I want to follow Time2Eat on social media
- As a user who has experienced any issues with the app or have any questions I want to be able to contact Time2Eat .

## Database Schema

![database](/static/img/database schema.jpg)

## Features

### In all pages

- **Favicon:** Appears in the page tab and has been created using the following favicon generator "https://favicon.io/favicon-generator/".

- **Navigation bar:** I have created the navigation bar using [Materialise](<[https://materializecss.com/](https://materializecss.com/)>) nav bar with **Icon Links** and I have also included the **Mobile Collapse Button**. Then I have customised it to be in line with the website design

* **Mobile Collapse Button / Sidebar:** The **Mobile Collapse Button** will appear in smaller screens (tablets and mobiles) and by clicking on it, it will show the navigation bar as a sidebar.

- **Logo:** The logo will appear in the navigation bar for every section of the website and when clicked it will redirect the user to the home page (get_recipes.html) or to the login page if clicked from the "regiter" page.

- **[Material Icons:](https://material.io/)** They are used on the top navigation bar (for desktops and large desktops) and also in other sections of the website to add extra meaning.

- **[FontAwesome:](https://fontawesome.com/ "https://fontawesome.com/")** In some cases if FontAwesome icon was more appropriate I have also used FontAwesome (i.e. social media link icons, vote icon).

* **Social media links:** They appear on the page footer in every page on the website and by clicking on them the user will get re-directed to the media websites to follow Time2Eat. (since the website is fictitious they will be redirected to the login page for facebook or twitter).

* **Sticky Footer:** I have used the sticky footer from materialise to include the social media links and the contact details.
* **Contact Us:** Provides the user with the website contact details in case he/she wants to get in touch.

### login.html

- The login page has an input form where the users will enter their username and password. If the username is not registered or if the password is incorrect an error message will appear.
- New users can click on the link "Register here" to get redirected to the register page.

### register.html

- The new users will have to register using the input form in this page in order to start using the app. If the username entered in the form has already been used by another user then an error message indicating this issue will be displayed.
- In order to store the passwords securely in MongoDB, the passwords have been hashed using the bcrypt function.

### get_recipes.html

This in the home page where the carousel with all the recipes is displayed. In this page the user can search recipes entering words in the searh box and can also filter the recipes using the filter section under the carousel,

- **Search input box**: On the top left corner of the page the users can enter text to search for a specific word in the recipes data base. As a result all the recipes containing that word will be displayed. This can be very useful if you are looking for specific ingredients, name of authors, level of difficulty, cuisine, name of recipe or allergens.

- **Carousel:** The first time the user lands in this page will be able to see all the recipes available in the app by moving sideways using the carousel. The recipes in the carousel will be sorted by number of votes and then by number of views, being the recipe with more votes at the top of the carousel, then if the user moves in the carousel to the right the recipes will be sorted descending by number of votes and number of views and if the user moves to the left then the recipes will be sorted in ascending order.
  By clicking on the image or on the text "view" the user will be redirected to the "View_recipe.html" page where he/she can see all the details available for the recipe.
  At the bottom of the carousel the user can see how many votes and views each recipe has.

- **Filter form**: Below the carousel there is a section where the user can filter the results based on the following criteria:

  - **Switch “Only mine”** : The users can activate this switch if they only want to see their own recipes.

  - **Select drop-down menu to filter by difficulty:** I have used the select option from materialize to allow the user to filter by difficulty. This filter can be used on its own or as a combination with more filters in the filter section.
  - **Select dropdown menu to filter by cuisine** : I have used the select option from materialize to allow the user filter by cuisine. This filter can be used on its own or as a combination with more filters in the filter section.
  - **Filter by recipes that don't have certain allergens:** I have added check boxes with the main allergens so the user can select which allergens should be removed from the results.
  - **Type of Meal**: The users can tick the checkboxes for the type of meal(s) that they are looking recipes for.

### View recipe page

This page will display the main attributes for the recipe. If the recipe belongs to the user he/she will have the options to remove or edit the recipe and if the recipes doesn't belong to the user then the user will have the option to vote for the recipe.

- **Delete button:** This button will only be visible if the recipe belongs to the user and will allow the user to remove the recipe.
  Before the recipe gets removed a confirmation message will appear so the user can confirm if he/she wants to delete the recipe or not.

- **Edit button:** This button will only be visible if the recipe belongs to the user and will allow the user to edit the recipe by redirecting the user to the edit_recipe.html page.
- **Vote button:** This button will only be visible if the recipe doesn't belong to the user and by clicking on it the number of votes displayed at the right top of the screen will be incremented by one.
- **Modal:** When the user clicks on "delete button" the confirmation message will be display on a modal window. This modal has been taken from Materialize.

### add_recipe.html & edit_recipe.html

These pages will be used by the user to enter a new recipe or to edit an existing one.

- **Form:** The whole page is a form with different input types. The form used has been taken from Materialize.

- **Input (type text)** I have used input type text for name of the recipe and calories inputs. Name of recipes is required but calories is optional as no everyone may know that information about a recipe.

- **Modal:** When the user clicks on "Upload image" a modal window will appear containing the input (type file).

- **Input (type file):** Allows the user to upload an image for the recipe. By using JavaScript the image will be display as soon as the file is selected. This field is optional. If the user doesn't upload an image then a standard image will be used for the recipe.

- **Input (type number):** I have used input type number for the "serves" field. This field will be compulsory.

- **Select input:** I have used "single" select inputs for the fields "Difficulty", "Type of meal" and "Cuisine". All of them are compulsory as they will also be used in the dashboard section and in order to filter the recipes in the home page.
  I have also used "multiple" select input to select the allergens in the recipes. This field won't be required because the recipe may not contain any allergens.

- **Textarea:** I have used textareas for the fields "Instructions" and "Ingredients".
  These fields are compulsory because they are the most important information about any recipe.
  The user needs to enter every ingredient/instruction in a different line to make sure it displays nicely. In order to display it properly I have converted the text to an array separating every ingredient/instruction by "\n".

- **Button 'Add Recipe':** By clicking this button the form will be submitted and the recipe will be inserted into the database.
  After adding the recipe the user gets redirected to the recipe that he/she has just created.

### Manage categories

- **Input box** Allows the user to enter a new category or cuisine if the category/cuisine that they need is not already on the list displayed below.
- **Table** I'm using a table from Materialize in order to display the list of categories and cuisines.
  In the second column of the table the users can see how many recipes there are for each type of meal / cuisine.

### Tips page

This page is used to explain to the user how to use the app in order to get the most out of it.

- **Material Icons:** I have used material icons matching with the material icons in the nav bar in order to explain the functionality of each part of the website.
  For small screens since the navigation icons disappear from the navigation bar I have also hide the icons for the descriptions of each section.

### Statistics page

This page will give the user an idea of how many and what kind of recipes can be found in the app based on different criteria and also displays a ranking of the top 10 most rated authors.

All the graphics used in this pages have been created using dc/js and crossfilter so by clicking on any of them the rest of the charts will be updated automatically.

- **Reset button:** If the users have filtered the charts by clicking on them then they can reset them to the default values by clicking the "Reset" button.

- **Row Chart:** The row charts have been created to display the ranking of the top 10 voted authors and the cuisines available in the app.

- **Pie Chart** They have been used to display the number of recipes split by type of meal and by difficulty.

- **Summary table** The table contains additional information about the recipes filtered and it is sorted descending by number of votes. For each recipe in the table the user can click on the "View" link to get redirected to the recipe page.

## Features Left to Implement

- **Favourites:** I would like to save for each user their favourites recipes so they could save them and access them quicker.
- **Limit the Number of votes:** At the moment the users can vote a recipe more than once but in future I would like to make sure that a user can only vote the same recipe once.
- **Persistance of the filter when searching for recipes** After selecting some filter options and clicking on search I would like to make sure that the options selected on the filters stay selected.

## Technologies Used

#### Mock-up tool:

- **[Pencil:](https://pencil.evolus.vn/'https://pencil.evolus.vn/)** I have used Pencil to create the mock-ups for the website.

#### Graphic Design software:

- **[Adobe Fireworks:](https://www.adobe.com/products/fireworks.html)** I have used Adobe Fireworks to edit the background images, to create the logo and to do some edits on the mock-ups.

#### Languages:

- **HTML5:** Is the main language used to create the structure of the website.

- **CSS3:** Is the language used to add styles to the HTML.

- **[JavaScript:](https://developer.mozilla.org/en-US/docs/Web/JavaScript)** This is the language used to add interactivity to the website and to create the charts in the statistics page.

#### Libraries

- **[jQuery](https://jquery.com/)** This JavaScript library has been used to manipulate the DOM elements in a easier way than doing it with JavaScript.
- **[D3.js](https://d3js.org/)** JavaScript library is used to create the data visualizations on the "Statistics" page.
- **[DC.js](https://dc-js.github.io/dc.js/)** Is another JavaScript library that provides prebuilt chart types for D3.
- **[Crossfilter.js](http://crossfilter.github.io/crossfilter/)** Is a JavaScript library that allows the charts to be interactive and interdependent of the same dataset.
- **[queue.js](https://github.com/d3/d3-queue)** Is a JavaScript library that is needed in order to wait for the data to be fully loaded before the rest of the code is run.
- **[Material Icons:](<[https://material.io/tools/icons/?style=baseline](https://material.io/tools/icons/?style=baseline)>)** Has been used to add extra meaning on several parts of the website.
- **[FontAwesome:](https://fontawesome.com/ "https://fontawesome.com/")** In some cases if FontAwesome icon was more appropriate I have also used FontAwesome.
- **[Google Fonts:](https://fonts.google.com/ "https://fonts.google.com/")** I’ve used the fonts from Google Fonts to style the fonts in the website.
