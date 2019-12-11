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
  recipe_dictionary = recipe
  ingredient_dictionary = ingredients

  total = None
  for key in recipe_dictionary.keys():
    if key not in ingredient_dictionary:
      return False
    ##looking through keys associated with
    ## ingredients and if the specific key isn't
    ## in , return false
    total_AmtBatches = ingredient_dictionary[key]//recipe_dictionary[key]
    ##to get variable total_AmtBatches, you have to divide the individual ingredient key by the recipe key
    if total_AmtBatches == 0:
      return "No"
    # get zero as a result, no batches
    if not total:
      total = total_AmtBatches
    else:
      total = min(total, total_AmtBatches)
  return total

if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients =  { 'milk': 138, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))