from time import time
from datetime import datetime
from random import choice, choices, randint as rndi
from src.backend.game.card import Card
from src.backend.game.constants import CARDS




class __Store:
    MAX_CARDS = 5
    TIME_UNTIL_REROLL = 20
    def __init__(self):
        self.cards: list[Card] = []

        self.__rtime = time() + 20
    @property
    def reset_time(self):
        if time() >= self.__rtime:
            ...
    
    def get(self) -> dict:
        if self.reset_time <= time(): 
            self.reset_time = time() + 20
            self.cards.clear()
            for i in range(__Store.MAX_CARDS):
                self.cards.append(__Store.generateRandomCard())
        
        return {
            'cards': self.cards,
            'reset_time': datetime.fromtimestamp(self.reset_time)
        }
        

    def generateRandomCard(self) -> Card:
        keys = [k for k in CARDS]
        
        card_key: dict = choice(keys)
        card_dict = CARDS[card_key]
        weights = [i / 11 for i in range(11)]
        rarity = choice([i for i in range(11)])

        card = Card(
            card_key,
            card_dict['description'],
            cost = card_dict['cost'],
            img = card_dict['img'],
            rarity = rarity,
            owned = False
        )
        return card
    def reroll(self):
        self.cards.clear()
        for i in range(5):
            self.cards.append(
                self.generateRandomCard()
            )
        return ...
    def buy(self, id: int):
        card : Card
        card_id_l = [(card.id, idx) for card,idx in enumerate(self.cards) if card.id == id]
        if len(card_id_l) > 1 or not card_id_l:
            raise NotImplementedError()
        
        card_id, index = card_id_l[0]
        card = self.cards.pop(index)
        card.owned = True
        return
STORE = __Store()