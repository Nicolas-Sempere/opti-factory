# Opti-Factory
<i>Efficient production planning for Satisfactory: Minimize power, machines, and complexity with Python and PlantUML</i>

[Satisfactory](https://coffeestain.com/games/satisfactory) is a first-person open-world factory building game, developed and published by Coffee Stain Studios.

# Table of contents
1. [General Overview](#generalOverview)
1. [Detailed Overview](#detailedOverview)
1. [How to use](#howToUse)
1. [Examples of optimized production lines](#examples)
1. [Bottom-Up Algorithm for Optimizing Production Lines](#algorithmDescription)

## General Overview <a name="generalOverview"></a>
<p align="center">
<img src="images-for-readme/C4-System_Context.svg?raw=true" alt="drawing"/></p>
<p align="center"><ins>Overview of Opti-Factory</ins></p>

## Detailed Overview <a name="detailedOverview"></a>
<p align="center">
<img src="images-for-readme/C4-Container.svg?raw=true" alt="drawing"/></p>
<p align="center"><ins>Detailed overview of Opti-Factory</ins></p>

## How to use <a name="howToUse"></a>
### Requirements
- Python 3.12 (add it to the path)
- PlantUML (last version)
- A JRE (see PlantUML’s documentation for the correct version)

### Steps to execute the program
- Start PlantUML jar, then change directory to `production-lines`:
    - PNG output: ```java -jar plantuml.jar -charset utf-8 -gui -png```
    - SVG output: ```java -jar plantuml.jar -charset utf-8 -gui -svg```

- Configure the target product and target speed in `configuration.toml`.

- Start python either with:
   - the command line: ```python src/Main.py```, 
   - or the bat file `main.bat`

### Results
The output of the program is in `production-lines`.

### Adding or deleting recipes
The available recipes are stored in `src/gameData/RecipeDictionary.py`.
It is possible to add or delete available recipes in this file.


## Examples of optimized production lines <a name="examples"></a>
### Simple example: Iron Ingot x60
<p align="center">
<img src="images-for-readme/1st_Iron_Ingot_x60.svg?raw=true" alt="drawing"/></p>
<p align="center"><ins>Production line - Iron Ingot (60/min)</ins></p>

### A bit more complex example: Computer x1
<p align="center">
<img src="images-for-readme/1st_Computer_x1.svg?raw=true" alt="drawing"/></p>
<p align="center"><ins>Production line - Computer (1/min)</ins></p>


## Bottom-Up Algorithm for Optimizing Production Lines <a name="algorithmDescription"></a>
### Overview
The production lines optimization algorithm starts from the raw resources (leaves) and works its way up to the target product (root).
It selects the most efficient recipes at each step, ensuring minimal machine usage and power consumption.
- Inputs:
   - a target product
   - a target speed
- Output: a PlantUML diagram representing an optimized production line for the target product, at the target speed.

### Steps
1. **Identify Leaf Products**  
   The algorithm begins by identifying the **leaf products**, which are raw resources like iron mine, copper mine, oil pool, etc.
   These products don’t require *preprocessing* and are directly available.
   That is to say, there is no choice for their *recipe*.
   They are currently created with Mk.2 Extractors only.

2. **Optimize Leaves’ Parents Recipes**  
   For each leaf’s parent product (for example iron ore, copper ore, crude oil, etc), the algorithm selects the best recipe based on:
   - The number of machines required (n).
   - The power consumption (p).
   
   Concretely, the recipe which minimizes the euclidean norm of the point (n, p) is chosen.
   The optimal recipe for each leaf’s parent product is stored for use in the next steps.

3. **Repeat the Process**  
   The algorithm continues this process, moving upwards through the production line.
   For each product, it selects the most optimal recipe using the previously optimized inputs from the lower levels.

4. **Reach the Target Product**  
   Eventually, the algorithm reaches the target product specified by the user.
   At this point, it selects the optimal recipe for producing this product based on the fully optimized inputs from previous steps.

5. **Final Output**  
   The algorithm outputs a complete, optimized production line, which includes:
   - The number of machines and the power required at each step.
   - The inputs and outputs at every stage of the production line.