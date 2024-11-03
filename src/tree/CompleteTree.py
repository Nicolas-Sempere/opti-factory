from tree import Node
from tree.Tree import Tree
from tree.Node import ByproductNode, LeafNode, MachineNode, ProductNode


# An objective product can be made using n possible sets of recipes
# The complete tree represents all these possibilities
class CompleteTree(Tree):
    def __init__(self, objectiveProductName, objectiveSpeed):
        super().__init__(objectiveProductName, objectiveSpeed)

    def computeGraph(self, recipeProvider):
        self.computeGraphRecursion(
            self.objectiveProductName, self.objectiveSpeed, -1, recipeProvider
        )

    def computeGraphRecursion(
        self, productName, productSpeed, parentIndex, recipeProvider
    ):
        recipesDictionary = recipeProvider.getRecipesDictionary()
        if productName in recipesDictionary:
            ### Creation of the "product" node
            productIndex = len(self.graph)
            self.graph[productIndex] = ProductNode(
                productIndex, productName, parentIndex
            )

            for i in range(len(recipeProvider.getProductRecipes(productName))):
                machineInputs = recipeProvider.getInputs(productName, i)
                machineName = recipeProvider.getMachineName(productName, i)
                machineSpeed = recipeProvider.getOutputSpeed(productName, i)
                speedCoefficient = productSpeed / machineSpeed

                ### Creation of the "machine" node
                machineIndex = len(self.graph)
                dicoIndex = recipeProvider.getDicoIndex(productName, i)
                byproduct = recipeProvider.getByproduct(dicoIndex)
                hasByproduct = len(byproduct) > 0

                ### Creation of the "byproduct" node
                byproductNode = None
                if hasByproduct:
                    byproductIndex = len(self.graph) + 1
                    byproductName = byproduct[0]
                    byproductSpeed = byproduct[1] * speedCoefficient
                    byproductNode = ByproductNode(byproductIndex, byproductName)
                    byproductNode.addChild(machineIndex, byproductSpeed)
                    self.graph[byproductIndex] = byproductNode
                self.graph[machineIndex] = MachineNode(
                    machineIndex,
                    machineName,
                    productIndex,
                    speedCoefficient,
                    dicoIndex,
                    byproductNode,
                )

                ### Adding the machine to the children of the "product" node
                self.graph[productIndex].addChild(machineIndex, productSpeed)

                for machineInput in machineInputs:
                    inputProduct = machineInput[0]
                    inputSpeed = machineInput[1]

                    ### Adding the children products to the children of the "machine" node
                    childrenIndex = len(self.graph)
                    self.graph[machineIndex].addChild(
                        childrenIndex, speedCoefficient * inputSpeed
                    )

                    self.computeGraphRecursion(
                        inputProduct,
                        speedCoefficient * inputSpeed,
                        machineIndex,
                        recipeProvider,
                    )
        else:
            ### Creating a leaf of the tree
            leafIndex = len(self.graph)
            self.graph[leafIndex] = LeafNode(leafIndex, productName, parentIndex)

    def computeNumberOfPossibilities(self, productName, recipesDictionary):
        res = 0
        if productName in recipesDictionary:
            for i in range(len(recipesDictionary[productName])):
                method = recipesDictionary[productName][i]
                machineInputs = method[0]
                temp = 1
                for machineInput in machineInputs:
                    inputProduct = machineInput[0]
                    temp *= self.computeNumberOfPossibilities(
                        inputProduct, recipesDictionary
                    )
                res += temp
            return res
        else:
            return 1

    def getSubTreeNumberOfMachines(self, subTreeKeys):
        number = 0
        for key in subTreeKeys:
            node = self.getNode(key)
            if isinstance(node, Node.MachineNode):
                number += node.getNumber()
        return number

    def getSubTreeMachineKeys(self, subTreeKeys):
        res = []
        for key in subTreeKeys:
            node = self.getNode(key)
            if isinstance(node, Node.MachineNode):
                res.append(key)
        return res

    def getSubTreePowerConsumption(self, subTreeKeys):
        power = 0
        for key in subTreeKeys:
            node = self.getNode(key)
            if isinstance(node, Node.MachineNode):
                power += node.getPowerRequired()
        return power

    def getSubTreeObjectiveProductMachineNode(self, subTreeKeys):
        objectiveProductNode = self.getNode(0)
        objectiveProductMachines = objectiveProductNode.getChildrenList()
        for subTreeKey in subTreeKeys:
            for machineKey in objectiveProductMachines:
                if subTreeKey == machineKey:
                    return self.getNode(subTreeKey)
