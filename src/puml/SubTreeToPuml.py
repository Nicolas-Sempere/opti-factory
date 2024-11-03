import util.Util as Util
from puml.TreeToPuml import TreeToPuml


class SubTreeToPuml(TreeToPuml):

    def __init__(self):
        self.showNodesIndex = False
        self.showDicoIndex = False
        self.showMachinesNumber = True
        self.showMachinesPower = True
        self.maxMessageLength = 20

    # Legend contains :
    #   - Number of machines
    #   - Power required
    def addLegend(self, puml, tree):
        puml.append("legend")
        numberOfMachines = tree.getNumberOfMachines()
        puml.append(
            "Total Number of Machines: " + str(Util.roundNumber(numberOfMachines))
        )
        powerRequired = tree.getPowerRequired()
        puml.append(
            "Total Power required: " + str(Util.roundNumber(powerRequired)) + " W"
        )
        puml.append("endlegend")
