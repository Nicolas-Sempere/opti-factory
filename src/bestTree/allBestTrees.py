from bestTree.bestTreeUtil import (
    computeBestTrees,
    computeCompleteTrees,
)
from puml.SubTreeToPuml import SubTreeToPuml
from recipe.RecipeProvider import RecipeProvider

NUMBER_OF_PRODUCTION_LINES = 1
SAVE_ALL_BEST_TREES = True


def computeAllBestTrees(targetSpeed, maxNumberOfLoops, saveRecipesScores, log):
    # Initialization
    recipeProvider = RecipeProvider()
    allProductsList = recipeProvider.getProductsList()
    subTreeToPuml = SubTreeToPuml()
    recipeDictionary = recipeProvider.getRecipesDictionary()
    completeTrees = computeCompleteTrees(allProductsList, targetSpeed)

    # At each step:
    # the products which respect "numberOfPossibilities <= numberOfRecipes",
    # have their best recipe left
    for _ in range(maxNumberOfLoops):
        computeBestTrees(
            recipeProvider,
            completeTrees,
            subTreeToPuml,
            recipeDictionary,
            NUMBER_OF_PRODUCTION_LINES,
            SAVE_ALL_BEST_TREES,
            saveRecipesScores,
            log,
        )
