TOML_COMMENT = "#"
TOML_EQUAL = " = "
TOML_BOOLEANS = {"true": True, "false": False}

DEFAULT_CONFIGURATION = {
    "target_product": "Iron Ingot",
    "target_speed": 60,
    "number_of_production_lines": 1,
    "log": True,
    "save_recipes_scores": False,
    "max_number_of_loops": 100,
    "save_complete_trees": False,
    "compute_all_best_trees": False,
}


def isConfigurationLegal(configuration):
    number_of_production_lines = configuration["number_of_production_lines"]
    if number_of_production_lines > 10:
        print(
            "Error: the maximum number of production lines is 10,",
            number_of_production_lines,
            "was given.",
        )
        return False
    return True


# Parses the toml configuration file
def parseTomlConfiguration(tomlFileName):
    configuration = DEFAULT_CONFIGURATION
    with open(tomlFileName, "r") as tomlFile:
        for line in tomlFile:
            if line[0] != TOML_COMMENT:
                for key in configuration:
                    if key in line:
                        value = line[len(key + TOML_EQUAL) :].strip()
                        # Booleans
                        if value in TOML_BOOLEANS:
                            configuration[key] = TOML_BOOLEANS[value]
                        # Integers
                        elif value.isdigit():
                            configuration[key] = int(value)
                        # Strings
                        else:
                            configuration[key] = value.replace('"', "")
    configurationLegal = isConfigurationLegal(configuration)
    return configuration, configurationLegal
