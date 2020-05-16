import numpy as np
recipes = np.genfromtxt('recipes.csv', delimiter=',')
print(recipes)
cupcakes = np.array([2, 0.75, 2, 1, 0.5 ])
cookies = np.array(recipes[2,:])

#3rd column represents eggs needed in each recipe
eggs = recipes[:,2]
print("no of eggs needed in each recipe: " + str(eggs))
one_egg_recipe = eggs==1
print("is this recipe 1-egged? " + str(one_egg_recipe))

double_batch = 2*cupcakes
grocery_list = cookies+double_batch
