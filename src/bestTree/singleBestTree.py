from bestTree.allBestTrees import computeBestTrees
from bestTree.bestTreeUtil import (
    computeCompleteTrees,
    computeSubTreesKeys,
    saveCompleteTree,
    saveTrees,
    showSubTreesScore,
)
from puml.SubTreeToPuml import SubTreeToPuml
from recipe.RecipeProvider import RecipeProvider
from recipe.RecipeScore import RecipeScore
from tree.CompleteTree import CompleteTree


def computeSingleBestTree(
    targetProduct,
    targetSpeed,
    numberOfProductionLines,
    maxNumberOfLoops,
    saveRecipesScores,
    log,
    save_complete_trees,
):
    # Initialization
    recipeProvider = RecipeProvider()
    childrenProductsList = recipeProvider.keepOnlyChildrenProducts(targetProduct)
    subTreeToPuml = SubTreeToPuml()
    completeTrees = computeCompleteTrees(childrenProductsList, targetSpeed)

    # Bottum-up algorithm
    for loop in range(maxNumberOfLoops):

        # Computes the number of production lines possible
        objectiveCompleteTree = CompleteTree(targetProduct, targetSpeed)
        recipeDictionary = recipeProvider.getRecipesDictionary()
        numberOfPossibilities = objectiveCompleteTree.computeNumberOfPossibilities(
            targetProduct, recipeDictionary
        )
        numberOfRecipes = recipeProvider.getNumberOfRecipes(targetProduct)

        # Saves the complete tree (representing all possibilities) at each step
        # This tree shall become simpler as more recipes are deleted
        if save_complete_trees:
            saveCompleteTree(
                objectiveCompleteTree, recipeProvider, numberOfPossibilities, loop, log
            )

        # If numberOfPossibilities <= numberOfRecipes
        # then all children products only have one recipe left (the best one)
        if numberOfPossibilities <= numberOfRecipes:
            objectiveCompleteTree.computeGraph(recipeProvider)
            subTreesKeys = computeSubTreesKeys(objectiveCompleteTree)
            subTreesScore = RecipeScore(objectiveCompleteTree, subTreesKeys)
            bestTreesIndices = subTreesScore.computeBestTreesIndices(
                numberOfProductionLines
            )
            bestTreesKeys = [subTreesKeys[i] for i in bestTreesIndices]

            if saveRecipesScores:
                showSubTreesScore(subTreesScore, bestTreesIndices, log)
            # Saves
            saveTrees(objectiveCompleteTree, bestTreesKeys, subTreeToPuml, log)
            break

        # For all the children products for which numberOfPossibilities <= numberOfRecipes,
        # only their best recipe is kept
        else:
            computeBestTrees(
                recipeProvider,
                completeTrees,
                subTreeToPuml,
                recipeDictionary,
                numberOfProductionLines,
                False,
                False,
                log,
            )
