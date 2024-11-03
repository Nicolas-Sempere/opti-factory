import util.Util as Util
import gameData.PowerDictionary as PowerDictionary


# A tree is made of different types of nodes :
#   - products
#   - machines
#   - leaves
class Node:
    def __init__(self, index, name, parentIndex):
        self.index = index
        self.name = name
        self.parents = [parentIndex]
        self.children = {}

    def addChild(self, childIndex, childSpeed):
        self.children[childIndex] = childSpeed

    def getParents(self):
        return self.parents

    def setParents(self, parents):
        self.parents = parents

    def addParents(self, parents):
        for parent in parents:
            self.parents.append(parent)

    def updateParent(self, oldIndex, newIndex):
        self.parents.append(newIndex)
        self.parents.remove(oldIndex)

    def getChildrenSpeeds(self):
        res = []
        for child in self.children:
            res.append(self.children[child])
        return res

    def getName(self):
        return self.name

    def getChildren(self):
        return self.children

    def getChildrenList(self):
        res = []
        for child in self.children:
            res.append(child)
        return res

    def setChildren(self, children):
        self.children = children

    def addChildren(self, newChildren):
        for newChild in newChildren:
            self.children[newChild] = newChildren[newChild]

    def addSpeeds(self, childrenToAdd):
        speedsToAdd = []
        for newChild in childrenToAdd:
            speedsToAdd.append(childrenToAdd[newChild])
        i = 0
        for currentChild in self.children:
            self.children[currentChild] += speedsToAdd[i]
            i += 1

    def updateChild(self, oldIndex, newIndex):
        self.children[newIndex] = self.children[oldIndex]
        del self.children[oldIndex]

    def getIndex(self):
        return self.index

    def setIndex(self, index):
        self.index = index

    def toString(self):
        res = "Index : " + Util.addSpaces(str(self.index), maxLength=3)
        res += "   |   Name : " + Util.addSpaces(str(self.name), maxLength=15)
        res += "   |   Children : "
        temp = ""
        for childIndex in self.children:
            temp += str(childIndex) + ":"
            temp += str(self.children[childIndex])
            temp += ", "
        temp = Util.addSpaces(temp[:-2], maxLength=10)
        res += temp
        res += "   |   Parents : "
        temp = ""
        for j in range(len(self.parents)):
            temp += str(self.parents[j]) + ", "
        temp = Util.addSpaces(temp[:-2], maxLength=10)
        res += temp
        print(res)


class MachineNode(Node):
    def __init__(self, index, name, parentIndex, number, dicoIndex, byproductNode):
        self.number = number
        self.dicoIndex = dicoIndex
        self.clockSpeed = 75
        self.effectiveNumber = self.number * (100 / self.clockSpeed)
        self.byproductNode = byproductNode
        Node.__init__(self, index, name, parentIndex)

    def getNumber(self):
        return self.number

    def addNumber(self, number):
        self.number += number

    def getDicoIndex(self):
        return self.dicoIndex
    
    def getPowerRequired(self):
        return self.number * PowerDictionary.InitialPowerUsages[self.name]
    
    def hasByproduct(self):
        return self.byproductNode != None
    
    def getByproductNode(self):
        return self.byproductNode
    


class ProductNode(Node):
    def __init__(self, index, name, parentIndex):
        Node.__init__(self, index, name, parentIndex)

    def updateChildSpeed(self, newSpeed):
        for child in self.children:
            self.children[child] = newSpeed


class LeafNode(Node):
    def __init__(self, index, name, parentIndex):
        Node.__init__(self, index, name, parentIndex)


class ByproductNode(Node):
    def __init__(self, index, name):
        Node.__init__(self, index, name, -2)