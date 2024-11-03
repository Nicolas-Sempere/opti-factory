from abc import abstractmethod

import util.Util as Util
import tree.Node as Node

OUTPUT_DIR = "production-lines/"
DEBUG = True


# Strategy Interface
class TreeToPuml:

    def __init__(self):
        pass

    def treeToPuml(self, tree, fileNamePrefix, log):
        puml = ["@startuml"]

        self.addFontSize(puml)
        self.addStyle(puml)
        self.addGraph(puml, tree)
        self.addLegend(puml, tree)

        puml.append("@enduml")

        self.writeFile(puml, tree, fileNamePrefix, log)

    @abstractmethod
    def addFontSize(self, puml):
        pass

    def addStyle(self, puml):
        puml.append("!include ../graphic-charter/opti_factory_style.iuml")

    def addGraph(self, puml, tree):
        links = []
        for key in tree.getKeys():
            self.addNode(tree.getNode(key), puml, links)
            self.addLinks(tree.getNode(key), links)
        for arrow in links:
            puml.append(arrow)

    def addNode(self, node, puml, links):
        if isinstance(node, Node.ProductNode):
            self.addProduct(puml, node)
        elif isinstance(node, Node.MachineNode):
            self.addMachine(puml, node)
            if node.hasByproduct():
                byProductNode = node.getByproductNode()
                self.addByproduct(puml, byProductNode)
                self.addLinks(byProductNode, links)

        elif isinstance(node, Node.LeafNode):
            self.addLeaf(puml, node)

    def addProduct(self, puml, productNode):
        res = "card " + str(productNode.getIndex())
        res += ' as "' + str(productNode.getName())[: self.maxMessageLength]
        if self.showNodesIndex:
            res += (
                "\n--\n<color $colors.yellow> Index: "
                + str(productNode.getIndex())
                + "</color>"
            )
        res += '"'
        puml.append(res)

    def addMachine(self, puml, machineNode):
        res = "usecase " + str(machineNode.getIndex())
        res += ' as "'
        if self.showMachinesNumber:
            res += str(Util.roundNumber(machineNode.getNumber())) + " "
        res += str(machineNode.getName())[: self.maxMessageLength]
        if self.showMachinesPower:
            res += "\n(" + str(Util.roundNumber(machineNode.getPowerRequired())) + " W)"
        if self.showDicoIndex:
            res += (
                "\n--\n<color $colors.yellow> Dico Index: "
                + str(machineNode.getDicoIndex())
                + "</color>"
            )
        if self.showNodesIndex:
            res += (
                "\n--\n<color $colors.yellow> Index: "
                + str(machineNode.getIndex())
                + "</color>"
            )
        res += '"'
        puml.append(res)

    def addLeaf(self, puml, leafNode):
        res = "node " + str(leafNode.getIndex())
        res += ' as "' + str(leafNode.getName())[: self.maxMessageLength]
        if self.showNodesIndex:
            res += (
                "\n--\n<color $colors.yellow> Index: "
                + str(leafNode.getIndex())
                + "</color>"
            )
        res += '"'
        puml.append(res)

    def addByproduct(self, puml, byproductNode):
        res = "storage " + str(byproductNode.getIndex())
        res += ' as "' + str(byproductNode.getName())[: self.maxMessageLength]
        if self.showNodesIndex:
            res += (
                "\n--\n<color $colors.yellow> Index: "
                + str(byproductNode.getIndex())
                + "</color>"
            )
        res += '"'
        puml.append(res)

    def addLinks(self, node, links):
        nodeIndex = node.getIndex()
        children = node.getChildren()
        for childIndex in children:
            res = ""
            speed = children[childIndex]
            res += str(childIndex) + "-->" + str(nodeIndex)
            if (
                len(children) > 1
                or isinstance(node, Node.MachineNode)
                or isinstance(node, Node.ByproductNode)
                or nodeIndex == 0
            ):
                res += ": " + str(Util.roundNumber(speed))
            links.append(res)

    @abstractmethod
    def addLegend(self, puml, tree):
        pass

    # Write file to OUTPUT_DIR
    def writeFile(self, puml, tree, fileNamePrefix, log):
        objectiveProductName = tree.getObjectiveProductName()
        targetSpeed = tree.getObjectiveSpeed()
        fileName = (
            str(fileNamePrefix)
            + objectiveProductName.replace(" ", "_")
            + "_x"
            + str(targetSpeed)
        )
        pumlExtension = ".puml"
        pumlFilePath = OUTPUT_DIR + fileName + pumlExtension
        if log:
            print("Writing to:", pumlFilePath)
        file = open(pumlFilePath, "w")
        file.write("\n".join(puml))
        file.close()
