from src.backend.common.fhandler import yaml_read
NEW_DATA = {
    "name": "",
    "xp": 0,
    "history": [],
    "coin": 0,
    "material": 0,
    'coin_multiplier': 1,
    'material_multiplier': 1,
    'rarity_min_value': 0,
    'xp_multiplier': 1
}
QUESTS = yaml_read('./src/xp_table.yml')
CARDS = yaml_read('./src/cards.yml')