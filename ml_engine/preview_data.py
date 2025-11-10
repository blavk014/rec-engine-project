import pandas as pd

apps_df = pd.read_csv('../data/apps.csv')
entertainment_df = pd.read_csv('../data/entertainment.csv')
products_df = pd.read_csv('../data/products.csv')
recipe_df = pd.read_csv('../data/recipe.csv')

print ("Apps:")
print (apps_df.head(),"\n")
print ("Entertainment:")
print (entertainment_df.head,"\n")
print ("Products:")
print (products_df.head,"\n")
print("Recipe:")
print (recipe_df.head,"\n")
