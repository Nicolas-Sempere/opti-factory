import tree.Node as Node
import util.Util as Util

DEBUG = False


class Tree:

    def __init__(self, objectiveProductName, objectiveSpeed):
        self.graph = {}
        self.objectiveProductName = objectiveProductName
        self.objectiveSpeed = objectiveSpeed
        self.objectiveIndex = -1

    def getObjectiveProductName(self):
        return self.objectiveProductName

    def getObjectiveSpeed(self):
        return self.objectiveSpeed

    def getKeys(self):
        return [*self.graph]

    def getNode(self, key):
        return self.graph[key]

    def getLength(self):
        return len(self.graph)

    def deleteNode(self, key):
        del self.graph[key]

    def getMachineKeys(self):
        res = []
        for key in self.getKeys():
            if isinstance(self.getNode(key), Node.MachineNode):
                res.append(key)
        return res

    def getProductAndLeavesKeys(self):
        res = []
        for key in self.getKeys():
            if isinstance(self.getNode(key), Node.ProductNode) or isinstance(
                self.getNode(key), Node.LeafNode
            ):
                res.append(key)
        return res

    def getNumberOfMachines(self):
        res = 0
        for key in self.getMachineKeys():
            res += self.graph[key].getNumber()
        return Util.roundNumber(res)

    def getPowerRequired(self):
        res = 0
        for key in self.getMachineKeys():
            res += self.graph[key].getPowerRequired()
        return Util.roundNumber(res)

    def toString(self):
        for key in self.graph:
            self.graph[key].toString()
