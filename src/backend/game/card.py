from src.backend.game.format_number import format_number
MAX_RARITY = 11
class Card:
    id = 0
    
    def __init__(self, title, description,cost, img,rarity):
        self.title = title
        self.description = description
        self.cost = cost
        self.rarity = rarity
        self.img = img
        self.id = Card.id
        Card.id += 1
    
    def todict(self) -> dict:
        return {
            'title': self.title,
            'description': self.description,
            'cost': format_number(self.costForRarityLevel),
            'rarity': self.rarityAsStr,
            'img': self.img,
            'id': self.id
        }
    
    def __debug(self):
        if self.description == '...': print(f"""\033[34m description of {self.title} is ...""")
        if self.cost == 0: print(f"""\033[34m cost of {self.title} is 0""")

    def upgradeRarity(self):
        if self.rarity + 1 > MAX_RARITY: return False
        if self.cost > PERSON.material: return False
        
        PERSON.material -= self.cost
        self.rarity += 1
        
        return True
    
    @property
    def costForRarityLevel(self) -> int:
        return self.cost ** (self.rarity + 1)
    
    @property
    def rarityAsStr(self) -> str:
        return ['common',
         'uncommon',
         'rare',
         'epic',
         'legendary',
         'mythic',
         'unique',
         'relic',
         'ancient',
         'cosmic',
         'divine'][self.rarity]