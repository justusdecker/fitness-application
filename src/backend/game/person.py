from yaml import safe_load, safe_dump
from os.path import isfile

from src.backend.game.history import History
from src.backend.game.constants import NEW_DATA, CARDS
from src.backend.game.card import Card
from src.backend.game.format_number import format_number
from src.backend.game.level_calculations import LevelAPI

class __Person:
    def __init__(self, name: str):
        self.name = name
        self.img = ""
        self.xp = 0
        self.coin = 0
        self.material = 0
        
        self.coin_multiplier = 1
        self.material_multiplier = 1
        self.rarity_min_value = 0
        self.xp_multiplier = 1
        
        self.cards = [Card(card_info, CARDS[card_info]['description'], CARDS[card_info]['cost'], CARDS[card_info]['img'], CARDS[card_info]['max_rarity']) for card_info in CARDS] # DEMO CARDS
        
        self.__load(name)
    
    def __load(self, name: str): 
        if not isfile(self.__savePath): # Create a new savefile if not exist
            with open(self.__savePath, 'x') as f:
                safe_dump(NEW_DATA, f)
                
        with open(self.__savePath) as f:
            data = safe_load(f)
        
        self.img = data['img']
            
        self.history = History(data['history'])
        self.coin = data['coin']
        self.material = data['material']
        self.xp = data['xp']
        
        
        self.coin_multiplier = data['coin_multiplier']
        self.material_multiplier = data['material_multiplier']
        self.rarity_min_value = data['rarity_min_value']
        self.xp_multiplier = data['xp_multiplier']
        
    def save(self):
        data = {
            'xp': self.xp,
            'coin': self.coin,
            'material': self.material,
            'history': self.history.get(),
            'name': self.name,
            'coin_multiplier': self.coin_multiplier,
            'material_multiplier': self.material_multiplier,
            'rarity_min_value': self.rarity_min_value,
            'xp_multiplier': self.xp_multiplier,
            'img': self.img
        }
        
        with open(self.__savePath, 'w') as f:
            safe_dump(data, f,encoding='utf-8')

    @property
    def xpPercentage(self):
        return LevelAPI.get_xp_percentage(self.xp)
    
    @property
    def xpMax(self):
        return LevelAPI.get_xp_max_for_current_level(self.xp)

    @property
    def formattedXP(self) -> str:
        return format_number(self.xp)
    
    @property
    def formattedXPMax(self) -> str:
        return format_number(self.xpMax)
    
    @property
    def level(self):
        return LevelAPI.get_current_level(self.xp)
    
    @property
    def formattedCoin(self) -> str:
        return format_number(self.coin)
    
    @property
    def formattedMaterial(self) -> str:
        return format_number(self.material)
    
    @property
    def __savePath(self) -> str:
        return f'./data/{self.name}.yml'
    


PERSON = __Person('Justus')