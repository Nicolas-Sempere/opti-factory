import matplotlib.pyplot as pl

import util.Util as Util

DEBUG = False
RECIPE_SCORES_FOLDER = "recipes_scores/"

# Class responsible for the visualizaton of recipes score (cf RECIPE_SCORES_FOLDER)
class RecipeScoreVisualizer:

    def __init__(self, treeScore, bestTreesIndices, log):
        self.treeScore = treeScore
        self.numbers = treeScore.getNumbers()
        self.powers = treeScore.getPowers()
        self.norms = treeScore.getNorms()
        self.bestTreesIndices = bestTreesIndices
        self.objectiveProductName = treeScore.getObjectiveProductName()
        self.targetSpeed = treeScore.getObjectiveSpeed()
        self.log = log

    def saveScorePyplot(self):
        if DEBUG:
            print("Number:", self.numbers)
        if DEBUG:
            print("Power:", self.powers)
        size = max(int(100 / len(self.norms)), 3)
        pl.scatter(self.numbers, self.powers, color="cyan", s=size)
        pl.scatter(self.getBestNumbers(), self.getBestPowers(), color="orange", s=size)
        pl.scatter(0, 0, color="black", s=size)
        pl.grid(True)
        if len(self.norms) < 50:
            for i in range(len(self.powers)):
                pl.text(
                    self.numbers[i],
                    self.powers[i],
                    self.getLabel(i),
                    fontsize=9,
                    ha="right",
                )
            for i in range(len(self.bestTreesIndices)):
                pl.text(
                    self.getBestNumbers()[i],
                    self.getBestPowers()[i],
                    self.getLabel(self.bestTreesIndices[i]),
                    fontsize=9,
                    ha="right",
                )
        pl.title(self.getTitle())
        pl.xlabel(self.getXLabel())
        pl.ylabel(self.getYLabel())
        pl.savefig(self.getOutputPath(RECIPE_SCORES_FOLDER, ".png"))
        pl.close()

    def getBestNumbers(self):
        res = []
        for i in self.bestTreesIndices:
            res.append(self.numbers[i])
        return res

    def getBestPowers(self):
        res = []
        for i in self.bestTreesIndices:
            res.append(self.powers[i])
        return res

    def getAllLabels(self):
        labels = []
        for i in range(len(self.norms)):
            labels.append(self.getLabel(i))
        return labels

    def getLabel(self, index):
        return str(Util.roundNumber(self.norms[index])) + " (v" + str(index) + ")"

    def getTitle(self):
        res = "Score of each recipe for: " + self.objectiveProductName
        res += " x" + str(self.targetSpeed)
        res += "\nEuclidean norm of the number of machines and the power"
        return res

    def getXLabel(self):
        return "Total number of machines"

    def getYLabel(self):
        return "Total power consumption (W)"

    def getOutputPath(self, folderName, fileExtension):
        res = folderName + self.objectiveProductName.replace(" ", "_")
        res += "_x" + str(self.targetSpeed) + fileExtension
        if self.log:
            print("Writing to:", res)
        return res
