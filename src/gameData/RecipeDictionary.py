# Recipes_Dictionary contains key / values pairs where:
# key = OutputProduct 
# values = [Recipe_1, Recipe_2, ..., Recipe_n]
#
# Where: [Recipe_n] = [[InputProduct_i, InputSpeed_i]], 
#                       "Machine",
#                       OutputSpeed,
#                       (optional) [Byproduct, ByproductSpeed]]_n
Recipes_Dictionary = {
    "Iron Plate": [
        [[["Iron Ingot", 50], ["Plastic", 10]], "Assembler", 75],
        [[["Iron Ingot", 30]], "Constructor", 20],
    ],
    "Iron Rod": [[[["Iron Ingot", 15]], "Constructor", 15]],
    "Screw": [
        [[["Iron Ingot", 12.5]], "Constructor", 50],
        [[["Iron Rod", 10]], "Constructor", 40],
    ],
    "Copper Sheet": [
        [[["Copper Ingot", 22.5], ["Water", 22.5]], "Refinery", 22.5],
        [[["Copper Ingot", 20]], "Constructor", 10],
    ],
    "Steel Beam": [[[["Steel Ingot", 60]], "Constructor", 15]],
    "Steel Pipe": [[[["Steel Ingot", 30]], "Constructor", 20]],
    "Concrete": [[[["Limestone", 45]], "Constructor", 15]],
    "Quartz Crystal": [
        [[["Raw Quartz", 67.5], ["Water", 37.5]], "Refinery", 52.5],
        [[["Raw Quartz", 37.5]], "Constructor", 22.5],
    ],
    "Silica": [[[["Raw Quartz", 22.5]], "Constructor", 37.5]],
    "Wire": [
        [[["Copper Ingot", 12], ["Caterium Ingot", 3]], "Assembler", 90],
        [[["Copper Ingot", 15]], "Constructor", 30],
    ],
    "Cable": [
        [[["Wire", 60]], "Constructor", 30],
        # [
        #     [["Quickwire", 7.5], ["Rubber", 5]], "Assembler", 27.5
        # ],
    ],
    "Quickwire": [[[["Caterium Ingot", 12]], "Constructor", 60]],
    "Empty Canister": [[[["Plastic", 30]], "Constructor", 60]],
    "Smart Plating": [[[["Reinforced Iron Plate", 2], ["Rotor", 2]], "Assembler", 2]],
    "Versatile Framework": [
        [[["Modular Frame", 2.5], ["Steel Beam", 30]], "Assembler", 5]
    ],
    "Automated Wiring": [[[["Stator", 2.5], ["Cable", 50]], "Assembler", 2.5]],
    "Reinforced Iron Plate": [
        [[["Iron Plate", 90], ["Screw", 250]], "Assembler", 15],
        [[["Iron Plate", 18.75], ["Wire", 37.5]], "Assembler", 5.625],
        [[["Iron Plate", 30], ["Screw", 60]], "Assembler", 5],
    ],
    "Modular Frame": [
        [[["Reinforced Iron Plate", 7.5], ["Screw", 140]], "Assembler", 5],
        [[["Reinforced Iron Plate", 3], ["Iron Rod", 12]], "Assembler", 2],
    ],
    "Encased Industrial Beam": [
        [[["Steel Beam", 24], ["Concrete", 30]], "Assembler", 6]
    ],
    "Compacted Coal": [[[["Coal", 25], ["Sulfur", 25]], "Assembler", 25]],
    "Rotor": [
        [[["Copper Sheet", 22.5], ["Screw", 195]], "Assembler", 11.25],
        [[["Iron Rod", 20], ["Screw", 100]], "Assembler", 4],
        [[["Steel Pipe", 10], ["Wire", 30]], "Assembler", 5],
    ],
    "Stator": [[[["Steel Pipe", 15], ["Wire", 40]], "Assembler", 5]],
    "Motor": [
        [
            [["Rotor", 3.75], ["Stator", 3.75], ["Crystal Oscillator", 1.25]],
            "Manufacturer",
            7.5,
        ],
        [[["Rotor", 10], ["Stator", 10]], "Assembler", 5],
    ],
    "AI Limiter": [[[["Copper Sheet", 25], ["Quickwire", 100]], "Assembler", 5]],
    "Circuit Board": [
        [[["Copper Sheet", 27.5], ["Silica", 27.5]], "Assembler", 12.5],
        [[["Copper Sheet", 15], ["Plastic", 30]], "Assembler", 7.5],
        # [[["Rubber", 30], ["Petroleum Coke", 45]], "Assembler", 5],
    ],
    "High-Speed Connector": [
        [
            [["Quickwire", 210], ["Cable", 37.5], ["Circuit Board", 3.75]],
            "Manufacturer",
            3.75,
        ],
        [
            [["Quickwire", 90], ["Silica", 37.5], ["Circuit Board", 3]],
            "Manufacturer",
            3,
        ]
    ],
    "Heavy Modular Frame": [
        [
            [
                ["Modular Frame", 18.75],
                ["Encased Industrial Beam", 11.25],
                ["Rubber", 75],
                ["Screw", 390],
            ],
            "Manufacturer",
            3.75,
        ],
        [
            [
                ["Modular Frame", 10],
                ["Steel Pipe", 30],
                ["Encased Industrial Beam", 10],
                ["Screw", 200],
            ],
            "Manufacturer",
            2,
        ],
    ],
    "Computer": [
        [
            [["Circuit Board", 25], ["Cable", 22.5], ["Plastic", 45], ["Screw", 130]],
            "Manufacturer",
            2.5,
        ],
        [[["Circuit Board", 7.5], ["Crystal Oscillator", 2.8125]], "Assembler", 2.8125],
    ],
    "Crystal Oscillator": [
        [
            [["Quartz Crystal", 18], ["Cable", 14], ["Reinforced Iron Plate", 2.5]],
            "Manufacturer",
            1,
        ]
    ],
    "Modular Engine": [
        [[["Motor", 2], ["Rubber", 15], ["Smart Plating", 2]], "Manufacturer", 1]
    ],
    "Adaptive Control Unit": [
        [
            [
                ["Automated Wiring", 7.5],
                ["Circuit Board", 5],
                ["Heavy Modular Frame", 1],
                ["Computer", 1],
            ],
            "Manufacturer",
            1,
        ]
    ],
    "Fabric": [[[["Polymer Resin", 30], ["Water", 30]], "Refinery", 30]],
    "Caterium Ingot": [
        [[["Caterium Ore", 45]], "Smelter", 15],
        [[["Caterium Ore", 24], ["Water", 24]], "Refinery", 12],
    ],
    "Plastic": [
        [[["Crude Oil", 30]], "Refinery", 20, ["Heavy Oil Residue", 10]],
        # [[["Polymer Resin", 60], ["Water", 20]], "Refinery", 20],
    ],
    "Rubber": [
        [[["Plastic", 30], ["Fuel", 30]], "Refinery", 60],
        [[["Crude Oil", 30]], "Refinery", 20, ["Heavy Oil Residue", 20]],
        # [[["Polymer Resin", 40], ["Water", 40]], "Refinery", 20],
    ],
    "Heavy Oil Residue": [[[["Crude Oil", 30]], "Refinery", 40, ["Polymer Resin", 20]]],
    "Petroleum Coke": [[[["Heavy Oil Residue", 40]], "Refinery", 120]],
    "Fuel": [
        [[["Heavy Oil Residue", 60]], "Refinery", 40],
        [[["Crude Oil", 60]], "Refinery", 40, ["Polymer Resin", 30]],
    ],
    "Turbofuel": [
        [[["Heavy Oil Residue", 37.5], ["Compacted Coal", 30]], "Refinery", 30]
    ],
    "Liquid Biofuel": [[[["Solid Biofuel", 90], ["Water", 45]], "Refinery", 60]],
    "Iron Ingot": [
        [[["Iron Ore", 35], ["Water", 20]], "Refinery", 65],
        [[["Iron Ore", 20], ["Copper Ore", 20]], "Foundry", 50],
        [[["Iron Ore", 30]], "Smelter", 30],
    ],
    "Copper Ingot": [
        [[["Copper Ore", 50], ["Iron Ore", 25]], "Foundry", 100],
        [[["Copper Ore", 30]], "Smelter", 30],
    ],
    "Steel Ingot": [
        [[["Iron Ore", 45], ["Coal", 45]], "Foundry", 45],
        [[["Iron Ore", 22.5], ["Compacted Coal", 11.25]], "Foundry", 37.5],
    ],
    "Iron Ore": [
        [[["Iron Mine", 1]], "Miner Mk.2", 120],
    ],
    "Copper Ore": [[[["Copper Mine", 1]], "Miner Mk.2", 120]],
    "Limestone": [[[["Limestone Mine", 1]], "Miner Mk.2", 120]],
    "Caterium Ore": [[[["Caterium Mine", 1]], "Miner Mk.2", 120]],
    "Sulfur": [[[["Sulfur Mine", 1]], "Miner Mk.2", 120]],
    "Coal": [[[["Coal Mine", 1]], "Miner Mk.2", 120]],
    "Raw Quartz": [[[["Quartz Mine", 1]], "Miner Mk.2", 120]],
    "Crude Oil": [
        [[["Oil Pool", 1]], "Oil Extractor", 120],
    ],
    "Water": [
        [[["Water Pool", 1]], "Water Extractor", 120],
    ],
}

Liquids = [
    "Water",
    "Crude Oil",
    "Heavy Oil Residue",
    "Liquid Biofuel",
    "Fuel",
    "Turbofuel",
]

Packager_Recipes = {
    "Packaged Water": [[[["Water", 60], ["Empty Canister", 60]], "Packager", 60]],
    "Packaged Oil": [[[["Crude Oil", 30], ["Empty Canister", 30]], "Packager", 30]],
    "Packaged Heavy Oil Residue": [
        [[["Heavy Oil Residue", 30], ["Empty Canister", 30]], "Packager", 30]
    ],
    "Packaged Liquid Biofuel": [
        [[["Liquid Biofuel", 40], ["Empty Canister", 40]], "Packager", 40]
    ],
    "Packaged Fuel": [[[["Fuel", 40], ["Empty Canister", 40]], "Packager", 40]],
    "Water": [[[["Packaged Water", 120]], "Packager", 120, ["Empty Canister", 120]]],
    "Crude Oil": [[[["Packaged Oil", 60]], "Packager", 60, ["Empty Canister", 60]]],
    "Heavy Oil Residue": [
        [[["Packaged Heavy Oil Residue", 20]], "Packager", 20, ["Empty Canister", 20]]
    ],
    "Liquid Biofuel": [
        [[["Packaged Liquid Biofuel", 60]], "Packager", 60, ["Empty Canister", 60]]
    ],
    "Fuel": [[[["Packaged Fuel", 60]], "Packager", 60, ["Empty Canister", 60]]],
}
