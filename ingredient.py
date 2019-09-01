from enum import Enum


# TODO: Do something with ingredient types later
class IngredientType(Enum):

    BASIC = 1
    MAIN = 2
    DISGUSTING = 3
    FUNNY = 4


class Ingredient:

    def __init__(self, name, rarity, ingredient_type):
        self.name = name
        self.rarity = rarity
        self.ingredient_type = ingredient_type

    @staticmethod
    def from_dict(source):
        return Ingredient(source['name'], source['rarity'], IngredientType(source['type']))

    def to_dict(self):
        val = {'name': self.name, 'rarity': self.rarity, 'type': self.ingredient_type.value}
        return val

    def __repr__(self):
        u"Ingredient(name={}, rarity={}, type={})" \
            .format(self.name, self.rarity, self.ingredient_type.value)
