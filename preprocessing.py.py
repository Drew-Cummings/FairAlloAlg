
import namegenerator
import random



utilities = [
"Artichoke",
"Arugula",
"Asparagus",
"Avocado",
"Bamboo Shoots",
"Bean Sprouts",
"Beans",
"Beet",
"Belgian Endive",
"Bell Pepper",
"Bitter Melon/Bitter Gourd",
"Bok Choy",
"Broccoli",
"Brussels Sprouts",
"Burdock Root",
"Cabbage",
"Calabash",
"Capers",
"Carrot",
"Cassava",
"Cauliflower",
"Celery",
"Celery",
"Celtuce",
"Chayote",
"Chinese Broccoli",
"Corn/Maize",
"Baby Corn",
"Cucumber",
"English Cucumber",
"Gherkin",
"Pickling Cucumbers",
"Daikon Radish",
"Edamame",
"Eggplant/Aubergine",
"Elephant Garlic",
"Endive",
"Curly/Frisee",
"Escarole",
"Fennel",
"Fiddlehead",
"Galangal",
"Garlic",
"Ginger",
"Grape Leaves",
"Green Beans/String Beans/Snap Beans",
"Wax Beans",
"Greens",
"Amaranth Leaves/Chinese Spinach",
"Beet Greens",
"Collard Greens",
"Dandelion Greens",
"Kale",
"Kohlrabi Greens",
"Mustard Greens",
"Rapini",
"Spinach",
"Swiss Chard",
"Turnip Greens",
"Hearts of Palm",
"Horseradish",
"Jerusalem Artichoke/Sunchokes",
"Jícama",
"Kale",
"Curly",
"Lacinato",
"Ornamental",
"Kohlrabi",
"Leeks",
"Lemongrass",
"Lettuce",
"Butterhead- Bibb",
"Iceberg",
"Leaf- Green Leaf",
"Romaine",
"Lotus Root",
"Lotus Seed",
"Mushrooms",
"Napa Cabbage",
"Nopales",
"Okra",
"Olive",
"Onion",
"Green Onions/Scallions",
"Parsley",
"Parsley Root",
"Parsnip",
"Peas",
"green peas",
"snow peas",
"sugar snap peas",
"Peppers",
"Plantain",
"Potato",
"Pumpkin",
"Purslane",
"Radicchio",
"Radish",
"Rutabaga",
"Sea Vegetables",
"Shallots",
"Spinach",
"Squash",
"Sweet Potato",
"Swiss Chard",
"Taro",
"Tomatillo",
"Tomato",
"Turnip",
"Water Chestnut",
"Water Spinach",
"Watercress",
"Winter Melon",
"Yams",
"Zucchini"]


def initialize(num_persons,num_utilities,utility_list):

    people = []
    utilities_chosen = []

    for i in range(num_persons):

        people.append(namegenerator.gen())


    for i in range(num_utilities):
        chosen_utility =random.choice(utility_list)
        utilities_chosen.append(chosen_utility)

    return people,utilities_chosen



def create_ratings(people,utilities_chosen):
    complete_rating = {}
    utility_rating= {}

    for i in people:
        for j in utilities_chosen:
          rating = random.randrange(-10,10)
          utility_rating[j] = rating
        
        complete_rating[i] = utility_rating
    return complete_rating


people,utilities_chosen = initialize(4,2,utilities)

print(create_ratings(people,utilities_chosen))








