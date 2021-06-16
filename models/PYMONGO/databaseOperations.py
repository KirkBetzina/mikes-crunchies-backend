import pymongo
from pymongo import collection
from bson import ObjectId
#CONNECT TO DATABASE
connection = pymongo.MongoClient('localhost', 27017)
#CREATE DATABASE
database = connection['mikes-crunchies-backend']
#CREATE COLLECTION
collection = database['mikes-menu']
print('database connected')

data = {
     "data": [
    {
    "row_id":2,
    "Entry":"1",
    "Food":"Quaterback Crunchies",
    "Description":"Butterfly Potatoes",
    "Price":"$6.00"
    },
    {
    "row_id":3,
    "Entry":"2",
    "Food":"French Fries",
    "Description":"Shoestring French Fries",
    "Price":"$6.00"
    },
    {
    "row_id":4,
    "Entry":"3",
    "Food":"Spicy Calamari",
    "Description":"Served with our remoulade sauce",
    "Price":"$8.00"
    },
    {
    "row_id":5,
    "Entry":"4",
    "Food":"Laces",
    "Description":"A HUGE portion of crispy seasoned onion rings",
    "Price":"$8.00"
    },
    {
    "row_id":6,
    "Entry":"5",
    "Food":"Clam Strip Roll",
    "Description":"Jumbo clam strips served on a grilled and buttered roll",
    "Price":"$8.00"
    },
    {
    "row_id":7,
    "Entry":"6",
    "Food":"Lobster Roll",
    "Description":"Hot or Cold ",
    "Price":"Market Price"
    },
    {
    "row_id":8,
    "Entry":"7",
    "Food":"Fried Shrimp",
    "Description":"Breadded or Coconut served with our Pina Colada sauce or our Cocktail sauce",
    "Price":"$8.00"
    },
    {
    "row_id":9,
    "Entry":"8",
    "Food":"Jalapeno Poppers",
    "Description":"Jalepeno Business served with our Boom-Boom Sauce",
    "Price":"$6.00"
    },
    {
    "row_id":10,
    "Entry":"9",
    "Food":"Clam Fritters",
    "Description":"6 fluffy clam fritters ",
    "Price":"$5.00"
    },
    {
    "row_id":11,
    "Entry":"10",
    "Food":"Homemade Chowder",
    "Description":"add 3 fluffy clam fritters for $3.00 more",
    "Price":"$6.00"
    },
    {
    "row_id":12,
    "Entry":"11",
    "Food":"Garlic Knots",
    "Description":"Seasoned to perfection and served with our own Marinara",
    "Price":"$7.00"
    },
    {
    "row_id":13,
    "Entry":"",
    "Food":"WINGS"
    },
    {
    "row_id":14,
    "Entry":"12",
    "Food":"The Warm UP",
    "Description":"10 wings and 1 sauce of your choice",
    "Price":"$15.00"
    },
    {
    "row_id":15,
    "Entry":"13",
    "Food":"Pre-Game",
    "Description":"15 wings and 2 sauces of your choice",
    "Price":"$22.50"
    },
    {
    "row_id":16,
    "Entry":"14",
    "Food":"The Quater",
    "Description":"25 wings and 3 sauces of your choice",
    "Price":"$36.00"
    },
    {
    "row_id":17,
    "Entry":"15",
    "Food":"The Half",
    "Description":"50 wings and 4 sauces of your choice. Please allow for additional preperation time.",
    "Price":"$70.50"
    },
    {
    "row_id":18,
    "Entry":"16",
    "Food":"The Third Quarter",
    "Description":"75 wings and 5 sauces of your choice. Please allow for additional preperation time.",
    "Price":"$103.50"
    },
    {
    "row_id":19,
    "Entry":"17",
    "Food":"The Touchdown",
    "Description":"100 wings and 6 sauces of your choice. Please allow for additional preperation time.",
    "Price":"$133.00"
    },
    {
    "row_id":20,
    "Entry":"",
    "Food":"WING SAUCES"
    },
    {
    "row_id":21,
    "Entry":"18",
    "Food":"Memphis Sweet"
    },
    {
    "row_id":22,
    "Entry":"19",
    "Food":"Hickory Brown Sugar"
    },
    {
    "row_id":23,
    "Entry":"20",
    "Food":"Buffalo"
    },
    {
    "row_id":24,
    "Entry":"21",
    "Food":"Sweet Teriyaki"
    },
    {
    "row_id":25,
    "Entry":"22",
    "Food":"Carolina Gold"
    },
    {
    "row_id":26,
    "Entry":"23",
    "Food":"Garlic Parmesan"
    },
    {
    "row_id":27,
    "Entry":"24",
    "Food":"Carribean Jerk"
    },
    {
    "row_id":28,
    "Entry":"25",
    "Food":"Zesty Orange"
    },
    {
    "row_id":29,
    "Entry":"26",
    "Food":"Nashville Hot"
    },
    {
    "row_id":30,
    "Entry":"",
    "Food":"CHICKEN TENDERS"
    },
    {
    "row_id":31,
    "Entry":"27",
    "Food":"The Scrimmage",
    "Description":"3 chicken tenders includes a choice of ranch, bleu cheese or honey mustard dipping sauces or tossed with your favorite sauce.",
    "Price":"$5.15"
    },
    {
    "row_id":32,
    "Entry":"28",
    "Food":"The Kickoff",
    "Description":"5 chicken tenders includes a choice of ranch, bleu cheese or honey mustard dipping sauces or tossed with your favorite sauce.",
    "Price":"$8.10"
    },
    {
    "row_id":33,
    "Entry":"29",
    "Food":"The Offensive Line",
    "Description":"7 chicken tenders includes a choice of ranch, bleu cheese or honey mustard dipping sauces or tossed with your favorite sauce.",
    "Price":"$11.25"
    },
    {
    "row_id":34,
    "Entry":"30",
    "Food":"The Defensive Lone",
    "Description":"12 chicken tenders includes a choice of ranch, bleu cheese or honey mustard dipping sauces or tossed with your favorite sauce.",
    "Price":"$18.25"
    },
    {
    "row_id":35,
    "Entry":"",
    "Food":"SEAFOOD",
    "Description":"All seafood meals come with a choice of fries or quarterback crunchies, coleslaw, lemon wedge. Tartar sauce and malt vinegar upon request."
    },
    {
    "row_id":36,
    "Entry":"31",
    "Food":"Fish & Chips",
    "Description":"",
    "Price":"$10.95"
    },
    {
    "row_id":37,
    "Entry":"32",
    "Food":"Spicy Calamari Plate",
    "Description":"",
    "Price":"$10.95"
    },
    {
    "row_id":38,
    "Entry":"33",
    "Food":"Clam Strip Roll Plate",
    "Description":"",
    "Price":"$10.95"
    },
    {
    "row_id":39,
    "Entry":"34",
    "Food":"Fried Shrimp",
    "Description":"Breaded or Coconut",
    "Price":"$10.95"
    },
    {
    "row_id":40,
    "Entry":"35",
    "Food":"Whole Belly Clam Platter",
    "Description":"",
    "Price":"Market Price"
    },
    {
    "row_id":41,
    "Entry":"36",
    "Food":"Baked Haddock",
    "Description":"",
    "Price":"$10.95"
    },
    {
    "row_id":42,
    "Entry":"37",
    "Food":"Lobster Roll",
    "Description":"hot or cold",
    "Price":"Market Price"
    },
    {
    "row_id":43,
    "Entry":"",
    "Food":"SUBS"
    },
    {
    "row_id":44,
    "Entry":"38",
    "Food":"The Italian Stallion",
    "Description":"Capicola, Mortadella, Salama and Pepperoni MAMA-MIA",
    "Price":"$7.50"
    },
    {
    "row_id":45,
    "Entry":"39",
    "Food":"Veggie Sub",
    "Description":"choice of lettuce, pickles, onions, green peppers,tomatoes and olives",
    "Price":"$7.50"
    },
    {
    "row_id":46,
    "Entry":"40",
    "Food":"The Balboa",
    "Description":"Philly Cheese Steak with onions, peppers and mushrooms",
    "Price":"$8.00"
    },
    {
    "row_id":47,
    "Entry":"41",
    "Food":"Chicken Parmesan",
    "Description":"with sharp provolone",
    "Price":"$7.50"
    },
    {
    "row_id":48,
    "Entry":"42",
    "Food":"Eggplant Parmesan",
    "Description":"with sharp provolone",
    "Price":"$6.95"
    },
    {
    "row_id":49,
    "Entry":"43",
    "Food":"Blackened Chicken",
    "Description":"",
    "Price":"$7.50"
    },
    {
    "row_id":50,
    "Entry":"44",
    "Description":"Fish fried to perfection with lettuce, tomato and tartar sauce",
    "Price":"$7.95"
    },
    {
    "row_id":51,
    "Entry":"",
    "Food":"SMASHED BURGRS",
    "Description":"Cheese choices include American, Cheddar, and Swiss. Burger dressings include Mike’s Burger Sauce – recommended (mayo, ketchup, brown mustard Seasonings), ketchup, mustard, mayonnaise, or BBQ sauce. Unlimited toppings include grilled onions, grilled mushrooms, lettuce, pickles, raw onions "
    },
    {
    "row_id":52,
    "Entry":"",
    "Food":"",
    "Description":"***Mike’s meal deal: add your choice of Quarterback Crunchies or fries for",
    "Price":"$2.50"
    },
    {
    "row_id":53,
    "Entry":"45",
    "Food":"Single Burger",
    "Description":"",
    "Price":"$5.69"
    },
    {
    "row_id":54,
    "Entry":"46",
    "Food":"Single Cheeseburger",
    "Description":"",
    "Price":"$6.49"
    },
    {
    "row_id":55,
    "Entry":"47",
    "Food":"Single Bacon Burger",
    "Description":"",
    "Price":"$6.69"
    },
    {
    "row_id":56,
    "Entry":"48",
    "Food":"Single Bacon Cheeseburger",
    "Description":"",
    "Price":"$7.49"
    },
    {
    "row_id":57,
    "Entry":"49",
    "Food":"Double Burger",
    "Description":"",
    "Price":"$7.19"
    },
    {
    "row_id":58,
    "Entry":"50",
    "Food":"Double Cheeseburger",
    "Description":"",
    "Price":"$8.19"
    },
    {
    "row_id":59,
    "Entry":"51",
    "Food":"Double Bacon Burger",
    "Description":"",
    "Price":"$8.29"
    },
    {
    "row_id":60,
    "Entry":"52",
    "Food":"Double Bacon Cheeseburger",
    "Description":"",
    "Price":"$9.09"
    },
    {
    "row_id":61,
    "Entry":"",
    "Food":"PIZZA ",
    "Description":"Samll 12 | Large 16"
    },
    {
    "row_id":62,
    "Entry":"53",
    "Food":"Cheese and Tomato ",
    "Description":"Old World Tomato Sauce and Cheese",
    "Price":"S $7.95 | L $10.95"
    },
    {
    "row_id":63,
    "Entry":"54",
    "Food":"Meat Lovers",
    "Description":"Pepperoni, Sausage, Hamburger, Bacon",
    "Price":"S $11.95 | L $13.95"
    },
    {
    "row_id":64,
    "Entry":"55",
    "Food":"Veggie",
    "Description":"Onions, Peppers, Mushrooms, Sliced Tomato, Olives",
    "Price":"S $11.95 | L $13.95"
    },
    {
    "row_id":65,
    "Entry":"56",
    "Food":"Buffalo Chicken",
    "Description":"Zesty sauce with sliced white chicken, mozzarella, balsamic, red onion, drizzled with blue cheese dressing",
    "Price":"S $11.95 | L $13.95"
    },
    {
    "row_id":66,
    "Entry":"57",
    "Food":"White Clam",
    "Description":"Alfredo Clam Sauce, minced garlic, chopped Romano & Mozzarella",
    "Price":"S $11.95 | L $13.95"
    },
    {
    "row_id":67,
    "Entry":"58",
    "Food":"Hawaiian ",
    "Description":"Chorizo, lime, and infused pineapple pizza with Balsamic onions",
    "Price":"S $12.95 | L $14.95"
    },
    {
    "row_id":68,
    "Entry":"59",
    "Food":"The Camille",
    "Description":"Poached pears, Chorizo & goat cheese, topped with arugula and balsamic reduction",
    "Price":"S $12.95 | L $16.99"
    },
    {
    "row_id":69,
    "Entry":"60",
    "Food":"Chicken Bruschetta",
    "Description":"Sliced chicken breast topped with tomato bruschetta and balsamic glaze",
    "Price":"S $12.95 | L $14.95"
    },
    {
    "row_id":70,
    "Entry":"61",
    "Food":"CALZONE",
    "Description":"Every calzone is made with Ricotta and Mozzarella cheeses. Add $1 each for additional fillings.",
    "Price":"$8.95"
    },
   {
    "row_id":71,
    "Entry":"",
    "Food":"Toppings & FIllings",
    "Description":"Onions, Banana Peppers, Extra Cheese, Tomato Bruschetta, Green Pepper, Mushrooms, Hamburger Salami, Pepperoni, Sausage, Black Olives, Bacon"
    }]
}


collection.insert_one(data)

def insert_data(data):
    document = collection.insert_one(data)
    return document.inserted_id

def update_or_create(document_id, data):
    #TO AVOID DUPLICATES - THIS WILL CREATE A NEW DOCUMENT IF SAME ID DOESNT EXIST
    document = collection.update_one({'_id':ObjectId(document_id)},{'$set':data},upsert=True)
    return document.acknowledged

   

def remove_data(document_id):
    document = collection.delete_one({'_id':ObjectId(document_id)})
    return document.acknowledged
