import heapq

DEBUG = False

# Class responsible for the compution of recipes score
class RecipeScore:

    def __init__(self, completeTree, subTreesKeys):
        self.completeTree = completeTree
        self.subTreesKeys = subTreesKeys
        self.numbers = self.computeTreesNumberOfMachines()
        self.powers = self.computeTreesPower()
        self.norms = self.computeNorm()
        self.objectiveProductName = completeTree.getObjectiveProductName()
        self.targetSpeed = completeTree.getObjectiveSpeed()

    def computeBestTreesIndices(self, numberOfProductionLines):
        lowestNorms = heapq.nsmallest(numberOfProductionLines, self.norms)
        bestIndices = []
        for lowestNorm in lowestNorms:
            bestIndex = self.norms.index(lowestNorm)
            bestIndices.append(bestIndex)
        return bestIndices

    def computeTreesNumberOfMachines(self):
        number = []
        for subTreeKeys in self.subTreesKeys:
            number.append(self.completeTree.getSubTreeNumberOfMachines(subTreeKeys))
        return number

    def computeTreesPower(self):
        power = []
        for subTreeKeys in self.subTreesKeys:
            power.append(self.completeTree.getSubTreePowerConsumption(subTreeKeys))
        return power

    def computeNorm(self):
        maxPower = max(self.powers) * 2
        maxNumber = max(self.numbers) * 2
        res = []
        for i in range(len(self.numbers)):
            res.append(
                ((self.numbers[i] / maxNumber) + (self.powers[i] / maxPower)) * 100
            )
        return res

    def getNumbers(self):
        return self.numbers

    def getPowers(self):
        return self.powers

    def getNorms(self):
        return self.norms

    def getObjectiveProductName(self):
        return self.objectiveProductName

    def getObjectiveSpeed(self):
        return self.targetSpeed
