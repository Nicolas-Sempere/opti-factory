import copy

import tree.Tree as Tree

DEBUG = False
DEBUG2 = False
DEBUG3 = False
DEBUG_GET_SAME_MACHINE_KEYS = False


# A sub tree represents one possible set of recipes to make an objective product
# A sub tree is a subset of a complete tree, hence its name
class SubTree(Tree.Tree):
    def __init__(self, completeTree, subKeyList):
        Tree.Tree.__init__(
            self,
            completeTree.getObjectiveProductName(),
            completeTree.getObjectiveSpeed(),
        )
        self.computeGraph(completeTree, subKeyList)
        self.toDelete = []

    # Given a complete tree and a subset of it,
    # creates a sub tree, containing all the
    # nodes of the given subset
    def computeGraph(self, completeTree, subKeyList):
        for key in subKeyList:
            if DEBUG:
                print("\n")
            if DEBUG:
                print("key is :", key)
            newNode = copy.deepcopy(completeTree.getNode(key))
            if DEBUG:
                print("newNode is :")
            if DEBUG:
                newNode.toString()

            parents = newNode.getParents()
            if DEBUG:
                print("parents is :", parents)
            newParents = []
            for parent in parents:
                if parent in subKeyList:
                    newParents.append(parent)

            children = newNode.getChildren()
            newChildren = {}
            if DEBUG:
                print("Children is :", newNode.getChildren())
            for child in children:
                if child in subKeyList:
                    newChildren[child] = children[child]

            newNode.setParents(newParents)
            newNode.setChildren(newChildren)
            self.graph[key] = newNode

    # Groups a sub tree:
    # all identical machines, their inputs and outputs,
    # are grouped
    def group(self):
        sameMachinesKeys = self.getSameMachinesKeys()
        if DEBUG3:
            print("sameMachinesKeys is :", sameMachinesKeys)
        for i in range(len(sameMachinesKeys)):
            self.groupSameMachines(sameMachinesKeys[i])
        for indexToDelete in self.toDelete:
            self.deleteNode(indexToDelete)

    # Given a sub tree,
    # returns the indices of identical machines
    def getSameMachinesKeys(self):
        machineKeys = self.getMachineKeys()
        if DEBUG_GET_SAME_MACHINE_KEYS:
            print("machineKeys is :", machineKeys)
        sameMachinesKeys = []
        while len(machineKeys) > 0:
            if DEBUG_GET_SAME_MACHINE_KEYS:
                print("machineKeys is :", machineKeys)
            temp = []
            firstDicoIndex = self.getNode(machineKeys[0]).getDicoIndex()
            for j in range(1, len(machineKeys)):
                secondDicoIndex = self.getNode(machineKeys[j]).getDicoIndex()
                if firstDicoIndex == secondDicoIndex:
                    temp.append(machineKeys[j])
            if len(temp) != 0:
                temp.append(machineKeys[0])
                sameMachinesKeys.append(temp)
                if DEBUG_GET_SAME_MACHINE_KEYS:
                    print("temp is :", temp)
                if DEBUG_GET_SAME_MACHINE_KEYS:
                    print("sameMachinesKeys is :", sameMachinesKeys)
                for sameMachine in temp:
                    machineKeys.pop(machineKeys.index(sameMachine))
            else:
                machineKeys.pop(0)
        if DEBUG_GET_SAME_MACHINE_KEYS:
            print("sameMachinesKeys is :", sameMachinesKeys)
        return sameMachinesKeys

    # Given a list of identical machines indices,
    # groups all these machines in a single node
    def groupSameMachines(self, sameMachinesKeys):
        # The grouded machine node is the first one,
        # to which all the other machines are added
        groupedMachinesNode = self.getNode(sameMachinesKeys[0])
        groupedMachinesIndex = groupedMachinesNode.getIndex()

        # Adds all other machines to the first one
        for i in range(1, len(sameMachinesKeys)):
            # 0 - Gets the old machine
            oldIndex = sameMachinesKeys[i]
            machine = self.getNode(oldIndex)

            # 1 - Adds the old machine to grouped machine
            number = machine.getNumber()
            groupedMachinesNode.addNumber(number)

            # 2 - Adds and update the parent nodes :
            # their old child index, and their speed, are updated to the new ones
            machineParents = machine.getParents()
            groupedMachinesNode.addParents(machineParents)
            for parentIndex in machineParents:
                parentNode = self.getNode(parentIndex)
                parentNode.updateChild(oldIndex, groupedMachinesIndex)

            # 3 - Adds and update children nodes
            oldChildren = machine.getChildren()
            groupedMachinesNode.addSpeeds(oldChildren)
            newChildren = groupedMachinesNode.getChildren()
            childChildrenToAdd = []
            newChildrenList = groupedMachinesNode.getChildrenList()
            i = 0
            for child in oldChildren:
                childNode = self.getNode(child)
                childChildren = childNode.getChildren()
                childChildrenToAdd.append(childChildren)
                for childChild in childChildren:
                    childChildNode = self.getNode(childChild)
                    childChildNode.updateParent(child, newChildrenList[i])
                i += 1
            i = 0
            for child in newChildren:
                childNode = self.getNode(child)
                childNode.addChildren(childChildrenToAdd[i])
                i += 1

            # 4 - Adds the old machine to delete
            self.toDelete.append(oldIndex)

            # 5 - Adds the old children to delete
            for childIndex in oldChildren:
                self.toDelete.append(childIndex)
