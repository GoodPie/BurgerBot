import random
import sys

import facebook
import firebase
from ingredient import Ingredient, IngredientType

# Max amount of fillings allowed in a burger
MAX_FILLINGS = 5
WEIGHT_SCALE = 100


def create_new_filling(filling):
    """
    Sends a new filling to Firebase
    :param filling: Filling to add (Ingredient)
    :return:
    """
    ingredient_ref = firebase.db.collection(u'ingredients').document(filling.name)
    ingredient_ref.set(filling.to_dict())


def create_new_bun(bun):
    """
    Sends a new bun to Firebase
    :param bun: Bun to add (Ingredient)
    :return: 
    """
    bun_ref = firebase.db.collection(u'buns').document(bun.name)
    bun_ref.set(bun.to_dict())


def choose_fillings():
    """
    Chooses n random fillings from Firebase
    :return: Array of fillings
    """
    max_fillings = random.randint(1, MAX_FILLINGS)
    fillings_doc = firebase.db.collection(u'ingredients').stream()

    # Have to convert collection to array of dictionaries
    all_fillings = []
    for filling in fillings_doc:
        all_fillings.append(filling.to_dict())

    chosen_fillings = []
    for i in range(1, max_fillings):
        filling = choose_ingredient(all_fillings)
        all_fillings.remove(filling)  # So we don't have duplicate fillings
        chosen_fillings.append(filling)
        if len(all_fillings) == 0:
            # In case we go over filling limit
            break

    return chosen_fillings


def choose_bun():
    """
    Gets all the buns from Firebase and chooses a random one
    :return: Bun
    """
    bun_doc = firebase.db.collection(u'buns').stream()

    # Have to convert collection to array of dictionaries
    buns = []
    for bun in bun_doc:
        buns.append(bun.to_dict())

    return choose_ingredient(buns)


def create_burger():
    """
    Creates a juicy borger
    :return: Formatted version of the burger
    """

    # Choose a bun
    bun = choose_bun()

    # Choose some fillings
    fillings = choose_fillings()

    # Cook that nibba up
    burger = bun['name']
    for filling in fillings:
        burger += "\n{}".format(filling['name'])
    burger += "\n{}".format(bun['name'])

    return burger


def choose_ingredient(ingredients):
    """
    Chooses a random ingredient based on a list of ingredients based on its rarity

    :param ingredients: List of ingredients
    :return: Chosen ingredient
    """

    # First get the total weight of all ingredients we have and scale them with the lowest rarity being the most common
    total_weight = 0
    for i in ingredients:
        total_weight += WEIGHT_SCALE / int(i['rarity'])

    # Choose random value between those weights
    random_sel = random.uniform(0.0, total_weight)

    # Choose where that random value landed
    current_weight = 0
    for i in ingredients:
        current_weight += WEIGHT_SCALE / i['rarity']
        if random_sel < current_weight:
            return i


if __name__ == "__main__":

    if sys.argv[1].lower() == "--create" or sys.argv[1].lower() == "-c":
        burger = create_burger()
        print("Created burger: \n{}\n".format(burger))
        facebook.publish_burger_in_future(burger)
    elif sys.argv[1].lower() == "-f":
        filling_name = input("Enter ingredient name: ")
        filling_rarity = int(input("Enter ingredient rarity: "))
        filling_type = int(input("Enter ingredient type (Does nothing atm): "))

        ingredient = Ingredient(filling_name, filling_rarity, IngredientType(filling_type))
        create_new_filling(ingredient)
    elif sys.argv[1].lower() == "-b":
        bun_name = input("Enter bun name: ")
        bun_rarity = int(input("Enter bun rarity: "))
        bun_type = int(input("Enter bun type (1-3): "))

        bun = Ingredient(bun_name, bun_rarity, IngredientType(bun_type))
    else:
        print("""Usage: python BurgerBot.py [-options]
where options include:
    -c --create     Create a random burger and post it to Facebook
    -b              Create a new bun and add it to the database
    -f              Create a new filling and add it to the database
""")