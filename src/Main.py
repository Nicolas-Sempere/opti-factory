import sys

from bestTree.allBestTrees import computeAllBestTrees
from bestTree.singleBestTree import computeSingleBestTree
from util.ConfigurationParser import parseTomlConfiguration

CONFIGURATION_FILE = "configuration.toml"

if __name__ == "__main__":
    # Reads configuration file
    configuration, configurationLegal = parseTomlConfiguration(CONFIGURATION_FILE)
    if not configurationLegal:
        sys.exit()
    targetProduct = configuration["target_product"]
    targetSpeed = configuration["target_speed"]
    numberOfProductionLines = configuration["number_of_production_lines"]
    log = configuration["log"]
    saveRecipesScores = configuration["save_recipes_scores"]
    maxNumberOfLoops = configuration["max_number_of_loops"]
    save_complete_trees = configuration["save_complete_trees"]
    compute_all_best_trees = configuration["compute_all_best_trees"]

    # [/!\ Fun - Danger Zone /!\]
    # Computes the best production line for every product
    # that is present in Recipes_Dictionary (in gameData/RecipesDictionary.py)
    if compute_all_best_trees:
        computeAllBestTrees(targetSpeed, maxNumberOfLoops, saveRecipesScores, log)

    # Computes the "best tree" = "best production line"
    # for the target product at the target speed
    else:
        if log:
            print(
                "Computing",
                str(numberOfProductionLines),
                "best production lines for:",
                str(targetSpeed),
                str(targetProduct) + ".",
                "(Max number of loops:",
                str(maxNumberOfLoops) + ")",
            )

        computeSingleBestTree(
            targetProduct,
            targetSpeed,
            numberOfProductionLines,
            maxNumberOfLoops,
            saveRecipesScores,
            log,
            save_complete_trees,
        )
