# Cf satisfactory’s wiki - clock speed article
CONSTANT = 1.3219280948873624

# Discrete list of clock speeds
ClockSpeeds = [10, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250]

# Power usage for clock speed in ClockSpeeds list
PowerRanges = {
    "Constructor": [0.2, 0.6, 1.6, 2.7, 4, 5.4, 6.8, 8.4, 10, 11.7, 13.4],
    "Assembler": [0.7, 2.4, 6, 10.3, 15, 20.1, 25.6, 31.4, 37.5, 43.8, 50.4],
    "Manufacturer": [2.6, 8.8, 22, 37.6, 55, 73.9, 94, 115.3, 137.5, 160.7, 184.7],
    "Packager": [0.5, 1.6, 4, 6.8, 10, 13.4, 17.1, 21, 25, 29.2, 33.6],
    "Refinery": [1.4, 4.8, 12, 20.5, 30, 40.3, 51.3, 62.9, 75, 87.6, 100.7],
    "Smelter": [0.2, 0.6, 1.6, 2.7, 4, 5.4, 6.8, 8.4, 10, 11.7, 13.4],
    "Foundry": [0.8, 2.6, 6.4, 10.9, 16, 21.5, 27.3, 33.5, 40, 46.7, 53.7],
    "Miner Mk.2": [0.6, 1.9, 4.8, 8.2, 12, 16.1, 20.5, 25.1, 30, 35.1, 40.3],
    "Water Extractor": [0.7, 3.2, 8, 13.7, 20, 26.9, 34.2, 41.9, 50, 58.4, 67.2],
    "Oil Extractor": [1.9, 6.4, 16, 27.3, 40, 53.7, 68.4, 83.8, 100, 116.8, 134.3],
}

# Power usage at clock speed = 100%
InitialPowerUsages = {
    "Constructor": 4,
    "Assembler": 15,
    "Manufacturer": 55,
    "Packager": 10,
    "Refinery": 30,
    "Smelter": 4,
    "Foundry": 16,
    "Miner Mk.2": 12,
    "Water Extractor": 20,
    "Oil Extractor": 40,
    "Glacerie": 10,
}

PowerProducers = {
    "Coal Generator": [[[["Coal", 15], ["Water", 45]], 5]],
}
