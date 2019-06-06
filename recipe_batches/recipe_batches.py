#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    batches = []

    # Create lists to hold values for needed and available ingredients
    needed_ingredients = list(recipe.values())
    available_ingredients = list(ingredients.values())
    needed_key = list(recipe.keys())
    available_key = list(ingredients.keys())

    try:
        for x in range(0, len(needed_key)):
            if needed_key[x] != available_key[x]:
                return 0

        # If there are more values in the recipe than in the ingredients return 0
        if len(needed_ingredients) > len(available_ingredients):
            return 0

        for i in range(0, len(needed_ingredients)):
            # Divide value in available ingredients
            batches.append(available_ingredients[i] // needed_ingredients[i])

            if min(batches) < 1:
                return 0
        return min(batches)
    except IndexError:
        return 0


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
    ingredients = { 'milk': 132, 'butter': 158, 'flour': 51, 'sugar': 42, 'cacao': 12 }
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))