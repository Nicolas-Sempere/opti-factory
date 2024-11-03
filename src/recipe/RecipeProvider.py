import copy

import gameData.RecipeDictionary as RecipeDictionary


# Class responsible for the dynamic selection and deletion of recipes
class RecipeProvider:

    def __init__(self):
        self.recipesDictionary = copy.deepcopy(RecipeDictionary.Recipes_Dictionary)

    def keepOnlyChildrenProducts(self, targetProduct):
        childrenProducts = []
        self.getChildrenProducts(targetProduct, childrenProducts)
        productsToDelete = []
        for product in self.recipesDictionary:
            if product not in childrenProducts:
                productsToDelete.append(product)
        for productToDelete in productsToDelete:
            self.deleteProduct(productToDelete)
        return childrenProducts[1:]

    def getChildrenProducts(self, targetProduct, childrenProducts):
        if (
            targetProduct not in childrenProducts
            and targetProduct in self.recipesDictionary
        ):
            childrenProducts.append(targetProduct)
        if targetProduct in self.recipesDictionary:
            for i in range(len(self.getProductRecipes(targetProduct))):
                inputs = self.getInputs(targetProduct, i)
                for input in inputs:
                    self.getChildrenProducts(self.getInputName(input), childrenProducts)

    def getProductRecipes(self, productName):
        return self.recipesDictionary[productName]

    def deleteProduct(self, productName):
        del self.recipesDictionary[productName]

    def deleteRecipe(self, dicoIndex):
        productName = dicoIndex[0]
        indexToPop = dicoIndex[1]
        if len(self.recipesDictionary[productName]) > 1:
            self.recipesDictionary[productName].pop(indexToPop)

    def getByproduct(self, dicoIndex):
        productName = dicoIndex[0]
        index = dicoIndex[1]
        if len(RecipeDictionary.Recipes_Dictionary[productName][index]) == 4:
            return RecipeDictionary.Recipes_Dictionary[productName][index][3]
        else:
            return []

    def getNumberOfRecipes(self, targetProduct):
        return len(self.recipesDictionary[targetProduct])

    def keepSingleRecipe(self, bestRecipeDicoIndex):
        productName = bestRecipeDicoIndex[0]
        index = bestRecipeDicoIndex[1]
        self.recipesDictionary[productName] = [
            self.recipesDictionary[productName][index]
        ]

    def getProductsList(self):
        return [*self.recipesDictionary]

    # Returns the recipe index in the original Recipes Dictionary
    def getDicoIndex(self, productName, index):
        for i in range(len(RecipeDictionary.Recipes_Dictionary[productName])):
            if (
                RecipeDictionary.Recipes_Dictionary[productName][i]
                == self.recipesDictionary[productName][index]
            ):
                return (productName, i)

    def getEmptyScores(self):
        scores = {}
        for product in self.recipesDictionary:
            emptyScore = [0 for _ in range(len(self.recipesDictionary[product]))]
            scores[product] = emptyScore
        return scores

    def setRecipesDictionary(self, recipesDictionary):
        self.recipesDictionary = recipesDictionary

    def getRecipesDictionary(self):
        return self.recipesDictionary

    def getInputs(self, productName, recipeIndex):
        return self.recipesDictionary[productName][recipeIndex][0]

    def getInputName(self, input):
        return input[0]

    def getInputSpeed(self, input):
        return input[1]

    def getMachineName(self, productName, recipeIndex):
        return self.recipesDictionary[productName][recipeIndex][1]

    def getOutputSpeed(self, productName, recipeIndex):
        return self.recipesDictionary[productName][recipeIndex][2]

    def toString(self):
        for key in self.recipesDictionary:
            print(key)
            for recipe in self.recipesDictionary[key]:
                print("--->" + str(recipe))
