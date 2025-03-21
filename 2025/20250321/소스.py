#https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/submissions/1581147457/?envType=daily-question&envId=2025-03-21
#2115. Find All Possible Recipes from Given Supplies
from collections import defaultdict
from collections import deque

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        #topological sort 형식으로 해야 하나? 
        
        set_recipes = set(recipes)
        set_supplies = set(supplies)
        outgoing_edges = defaultdict(list)
        required_recipes = {recipe: [] for recipe in recipes}
        required_ingredients = defaultdict(list)
        for recipe, ingredient_list in zip(recipes, ingredients):
            for ingredient in ingredient_list:
                if ingredient in set_recipes:
                    required_recipes[recipe].append(ingredient)
                    outgoing_edges[ingredient].append(recipe)
                else:
                    required_ingredients[recipe].append(ingredient)


        myqueue = deque([])
        answer = []
        for recipe, required_recipe_list in sorted(required_recipes.items(), key = lambda a: len(a[1])):
            if required_recipe_list:
                break
            
            is_possible = True
            for ingredient in required_ingredients[recipe]:
                if ingredient not in set_supplies:
                    is_possible = False
                    break
            
            if not is_possible:
                continue
            
            myqueue.append(recipe)
            answer.append(recipe)

        while myqueue:
            curr = myqueue.popleft()
            for neighbor in outgoing_edges[curr]:
                required_recipes[neighbor].pop(required_recipes[neighbor].index(curr))
                if not required_recipes[neighbor]:
                    is_possible = True
                    for ingredient in required_ingredients[recipe]:
                        if ingredient not in set_supplies:
                            is_possible = False
                            break
                    if is_possible:
                        answer.append(neighbor)
                        myqueue.append(neighbor)

        return answer