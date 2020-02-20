#!/usr/bin/python

import math

#STEPS

# 1) Write a function that receives a recipe in
# the form of a dictionary, as well as all of
# the ingredients you have available to you,
# also in the form of a dictionary.

# 2) The keys will be the ingredient names, with
# their associated values being the amounts.

# 3) Your function should output the maximum
#  number of whole batches that can be made for
#  the supplied recipe using the ingredients
#  available to you, as indicated by the
#  second dictionary



def recipe_batches(recipe, ingredients):

  total = None

  for key in recipe.keys():
    if key not in ingredients:
      return 0
    batches = ingredients[key]//recipe[key]
    if batches == 0:
      return 0
    if not total:
      total = batches
    else:
      total = min(total, batches)
  return total

if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients =  { 'milk': 138, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))