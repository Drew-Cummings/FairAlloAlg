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
        counter = 0
        chosen_utility =random.choice(utility_list)
        if chosen_utility not in utilities_chosen:
            utilities_chosen.append(chosen_utility)
        else:
            utilities_chosen.append(chosen_utility + str(counter))
            counter += 1


    return people,utilities_chosen




def preprocessing(utilities_chosen):
    res = dict()
    for i in utilities_chosen:
        res[i] = random.randint(-10,10)
    return res



def final_preprocessing(num_person,num_utilities,utility_list):
    people,utilities_chosen = initialize(num_person,num_utilities,utility_list)

    preprocessing_final = {}
    for i in people:

        utility_ratings = preprocessing(utilities_chosen)
        preprocessing_final[i] = utility_ratings

    print(preprocessing_final)
    return preprocessing_final


# an example of the function call youll need to make
#THIS IS THE ONLY FUNCTION CALL YOU SHOULD NEED TO MAKE FOR PRE PROCESSING
#final_processing(number of people, number of utilities, the full utility list)
#Example: 
#final_preprocessing(5,50,utilities)