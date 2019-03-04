#Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.
def cakes(recipe, available):
    # TODO: insert code
    diction = {}
    for i in recipe.keys():
      if i in available.keys():
        continue
      else:
        return 0
    for i in recipe.keys():
      diction[i] = available[i] // recipe[i]
    return (min(diction.values()))
recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
cakes(recipe, available)
