from src.build_flask import *
from src.backend.common.fhandler import file_read
from yaml import safe_load
from src.backend.game.person import Person
from time import time
with open('./src/xp_table.yml', encoding='utf-8') as f:
    QUESTS = safe_load(f)

with open('./src/cards.yml', encoding='utf-8') as f:
    CARDS = safe_load(f)

def format_number(n):
    # Liste der Einheiten (kann beliebig erweitert werden)
    suffixes = ["", "K", "M", "B", "T", "Qa", "Qi", "Sx", "Sp", "O", "N", "Dc", "UDc", "DDc", "TDc", "QaDc", "QiDc", "SxDc", "SpDc", "ODc"]
    
    if n == 0:
        return "0"
    
    # Bestimme den Index für das Suffix (jede Stufe ist 1000x größer)
    import math
    suj_index = 0
    if n > 0:
        suj_index = int(math.floor(math.log10(abs(n)) / 3))
    
    if suj_index >= len(suffixes):
        suj_index = len(suffixes) - 1
        
    if suj_index == 0:
        return str(int(n))
    
    # Berechne den verkürzten Wert
    scaled_value = n / (10 ** (3 * suj_index))
    
    # Formatiere auf 2 Nachkommastellen (kannst du anpassen, z.B. .1f für eine Nachkommastelle)
    return f"{scaled_value:.2f}{suffixes[suj_index]}"

class Card:
    def __init__(self, title, description,cost, img,rarity):
        self.title = title
        self.description = description
        self.cost = cost
        self.rarity = rarity
        self.max_powerup = 0
        self.img = img
    
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
        
ALL_CARDS = [Card(card_info, CARDS[card_info]['description'], CARDS[card_info]['cost'], CARDS[card_info]['img'], CARDS[card_info]['max_rarity']) for card_info in CARDS]
PERSON = Person('Justus')
def get_level(xp: int):
    return xp // 250

def get_xp_for_level(xp: int):
    return xp % 250

def get_xp_max(xp: int):
    return (get_level(xp) + 1) * 250

@app.route('/game/buy/<key>',methods = [GET])
def game_buy(key: str):
    print(key)
    
    PERSON.xp += QUESTS[key]['xp']
    PERSON.coin += QUESTS[key]['coin'] if 'coin' in QUESTS[key] else 0
    PERSON.material += QUESTS[key]['material'] if 'material' in QUESTS[key] else 0
    PERSON.history.add(int(time()*1000), key)
    PERSON.save()
    return redirect('/game')

@app.route('/api/get')
def api_get():
    data = request.args.get('data')
    if data is None: raise NotImplementedError()
    return jsonify(
        {
            'coin': PERSON.coin,
            'material': PERSON.material
        }
    )

@app.route('/api/increase')
def api_increase():
    data = request.args.get('data')
    if data is None: raise NotImplementedError()
    PERSON.coin += 1
    PERSON.save()
    return "", 200

@app.route('/game',methods = [GET])
def game_index():

    
        
    xpbf = get_xp_for_level(PERSON.xp)
    xpbf = xpbf / 250 if xpbf else 0
    xpbf *= 100
    
    return render_template(
        'game/index.html',
        name= PERSON.name,
        level = get_level(PERSON.xp),
        current_xp = PERSON.xp,
        max_xp = get_xp_max(PERSON.xp),
        coin = PERSON.coin,
        material = PERSON.material,
        quests = QUESTS,
        xp_bar_fill = xpbf,
        history_count = PERSON.history.count(),
        cards= ALL_CARDS,
        format_number = format_number) 