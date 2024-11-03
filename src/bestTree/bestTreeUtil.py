from puml.CompleteTreeToPuml import CompleteTreeToPuml
from recipe.RecipeScore import RecipeScore
from tree import SubTreeUtil
from tree.CompleteTree import CompleteTree
from tree.SubTree import SubTree
from recipe.RecipeScoreVisualizer import RecipeScoreVisualizer

Ordonnals = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th"]

def computeBestTrees(
    recipeProvider,
    completeTrees,
    subTreeToPuml,
    recipeDictionary,
    numberOfProductionLines,
    saveAllBestTrees,
    saveRecipesScores,
    log,
):
    childrenProductsToDelete = []
    for childrenProduct in completeTrees:
        completeTree = completeTrees[childrenProduct]
        numberOfPossibilities = completeTree.computeNumberOfPossibilities(
            childrenProduct, recipeDictionary
        )
        numberOfRecipes = recipeProvider.getNumberOfRecipes(childrenProduct)
        if numberOfPossibilities <= numberOfRecipes:
            completeTree.computeGraph(recipeProvider)
            subTreesKeys = computeSubTreesKeys(completeTree)

            subTreesScore = RecipeScore(completeTree, subTreesKeys)
            bestTreesIndices = subTreesScore.computeBestTreesIndices(
                numberOfProductionLines
            )
            bestTreesKeys = [subTreesKeys[i] for i in bestTreesIndices]
            if saveAllBestTrees:
                if saveRecipesScores:
                    showSubTreesScore(subTreesScore, bestTreesIndices, log)
                saveTrees(completeTree, bestTreesKeys, subTreeToPuml, log)

            objectiveProductMachine = (
                completeTree.getSubTreeObjectiveProductMachineNode(bestTreesKeys[0])
            )
            bestRecipeDicoIndex = objectiveProductMachine.getDicoIndex()
            recipeProvider.keepSingleRecipe(bestRecipeDicoIndex)

            childrenProductsToDelete.append(childrenProduct)

    for childrenProduct in childrenProductsToDelete:
        del completeTrees[childrenProduct]


def computeCompleteTrees(objectiveProductsList, targetSpeed):
    completeTrees = {}
    for targetProduct in objectiveProductsList:
        completeTree = CompleteTree(targetProduct, targetSpeed)
        completeTrees[targetProduct] = completeTree
    return completeTrees


def computeSubTreesKeys(completeTree):
    branches = {}
    SubTreeUtil.computeBranches(branches, completeTree)
    startingIndex = 0
    subTreesKeys = SubTreeUtil.computeSubTreesKeys(branches, startingIndex)
    return subTreesKeys


def showSubTreesScore(subTreesScore, bestTreesIndices, log):
    treeScoreVisualizer = RecipeScoreVisualizer(subTreesScore, bestTreesIndices, log)
    treeScoreVisualizer.saveScorePyplot()


def saveTrees(completeTree, bestTreesKeys, subTreeToPuml, log):
    for i in range(len(bestTreesKeys)):
        subTree = SubTree(completeTree, bestTreesKeys[i])
        subTree.group()
        subTreeToPuml.treeToPuml(subTree, Ordonnals[i] + "_", log)


def saveCompleteTree(
    objectiveCompleteTree, recipeProvider, numberOfPossibilities, loop, log
):
    objectiveCompleteTree.computeGraph(recipeProvider)
    completeTreeToPuml = CompleteTreeToPuml(numberOfPossibilities)
    completeTreeToPuml.treeToPuml(
        objectiveCompleteTree, "Complete_Tree_Loop_Number_" + str(loop) + "_", log
    )
