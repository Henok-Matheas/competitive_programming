class Solution:

    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]],
                       supplies: List[str]) -> List[str]:

        recipedict = {recipes[idx]: idx for idx in range(len(recipes))}
        supplyset = set(supply for supply in supplies)
        cantbemade = set()
        answer = []

        path = set()
        visited = set()

        def dfs(recipe):
            for ingredient in ingredients[recipedict[recipe]]:
                if ingredient in supplyset:
                    continue
                elif ingredient in recipedict:
                    if ingredient in path:
                        return False
                    elif ingredient in visited:
                        return False
                    if ingredient not in path and ingredient not in visited:
                        visited.add(ingredient)
                        path.add(ingredient)
                        dfs(ingredient)
                        if ingredient not in supplyset:
                            return False
                else:
                    return False
            supplyset.add(recipe)
            path.remove(recipe)

        for recipe in recipes:
            if recipe not in visited:
                visited.add(recipe)
                path.add(recipe)
                dfs(recipe)
        for recipe in recipes:
            if recipe in supplyset:
                answer.append(recipe)
        return answer
