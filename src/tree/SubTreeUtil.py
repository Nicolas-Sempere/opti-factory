DEBUG = False


# Branches is as follows :
# {output_i : [[machine_1, input_11, ..., input_1n], ..., [machine_n, input_n1, ..., input_nm]]}
def computeBranches(branches, completeTree):
    for productKey in completeTree.getProductAndLeavesKeys():
        productNode = completeTree.getNode(productKey)
        machines = productNode.getChildren()
        branches[productKey] = []

        for machineKey in machines:
            res = [machineKey]
            inputs = completeTree.getNode(machineKey).getChildren()
            for inputKey in inputs:
                res.append(inputKey)
            branches[productKey].append(res)


# Computes all the subsets of a complete tree
def computeSubTreesKeys(branches, rootIndex):
    subTreesKeys = computeSubTrees(branches, rootIndex)
    for subTreeKeys in subTreesKeys:
        subTreeKeys.append(0)
    return subTreesKeys


def computeSubTrees(branches, rootIndex):
    if DEBUG:
        print("\n---\nStarting Index is : ", rootIndex, "\n")
    if len(branches[rootIndex]) == 0:
        return []

    res = []
    for branch in branches[rootIndex]:

        if DEBUG:
            print("- Branch is :", branch)
        toMultiply = [[branch]]
        for i in range(1, len(branch)):
            toMultiply.append(computeSubTrees(branches, branch[i]))

        temp = cartesianProduct(toMultiply)
        if DEBUG:
            print("- temp is :", temp)
        res = union(res, temp)
        if DEBUG:
            print("- res is :", res)
    return res


def cartesianProduct(input):
    if DEBUG:
        print("cartesianProduct of :", input)
    inputWithoutEmpty = []
    for i in range(len(input)):
        if input[i] != []:
            inputWithoutEmpty.append(input[i])

    if len(inputWithoutEmpty) >= 2:
        res = inputWithoutEmpty[0]
        for i in range(1, len(inputWithoutEmpty)):
            newRes = []
            input_i = inputWithoutEmpty[i]
            for e in res:
                for e_i in input_i:
                    newRes.append(union(e, e_i))
            if DEBUG:
                print("newRes is :", newRes)
            res = newRes
        if DEBUG:
            print("cartesianProduct is 1 :", res)
        return res
    else:
        if DEBUG:
            print("cartesianProduct is 2 :", inputWithoutEmpty)
        return inputWithoutEmpty[0]


def union(array1, array2):
    res = []
    for e in array1:
        res.append(e)
    for e in array2:
        res.append(e)
    return res
