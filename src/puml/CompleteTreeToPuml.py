import util.Util as Util
from puml.TreeToPuml import TreeToPuml


class CompleteTreeToPuml(TreeToPuml):

    def __init__(self, numberOfPossibilities):
        self.showNodesIndex = False
        self.showDicoIndex = True
        self.showMachinesNumber = False
        self.showMachinesPower = False
        self.maxMessageLength = 20
        self.numberOfPossibilities = numberOfPossibilities

    def addFontSize(self, puml):
        puml.append("skinparam DefaultFontSize 16")

    # Legend contains only the number of possibilities
    def addLegend(self, puml, tree):
        puml.append("legend")
        puml.append(
            "Number of possibilities: "
            + Util.readableInteger(self.numberOfPossibilities)
        )
        puml.append("endlegend")
