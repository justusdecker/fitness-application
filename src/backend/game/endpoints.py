from src.build_flask import *
from time import time

from src.backend.game.api.main_api import GameAPI
from src.backend.game.level_calculations import LevelAPI
from src.backend.game.card import Card
from src.backend.game.constants import QUESTS, CARDS
from src.backend.game.person import PERSON

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
        
ALL_CARDS = [Card(card_info, CARDS[card_info]['description'], CARDS[card_info]['cost'], CARDS[card_info]['img'], CARDS[card_info]['max_rarity']) for card_info in CARDS]

@app.route('/game/buy/<key>',methods = [GET])
def game_buy(key: str):
    print(key)
    
    PERSON.xp += QUESTS[key]['xp']
    PERSON.coin += QUESTS[key]['coin'] if 'coin' in QUESTS[key] else 0
    PERSON.material += QUESTS[key]['material'] if 'material' in QUESTS[key] else 0
    PERSON.history.add(int(time()*1000), key)
    PERSON.save()
    return redirect('/game')

@app.route('/game',methods = [GET])
def game_index():

    
        
    xpbf = LevelAPI.get_xp_for_next_level(PERSON.xp)
    xpbf = xpbf / 250 if xpbf else 0
    xpbf *= 100
    
    return render_template(
        'game/index.html',
        name= PERSON.name,
        level = LevelAPI.get_current_level(PERSON.xp),
        current_xp = PERSON.xp,
        max_xp = LevelAPI.get_xp_max_for_current_level(PERSON.xp),
        coin = PERSON.coin,
        material = PERSON.material,
        quests = QUESTS,
        xp_bar_fill = xpbf,
        history_count = PERSON.history.count(),
        cards= ALL_CARDS,
        format_number = format_number) 