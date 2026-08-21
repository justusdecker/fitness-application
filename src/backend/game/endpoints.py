from src.build_flask import *
from time import time

from src.backend.game.api.main_api import GameAPI
from src.backend.game.level_calculations import LevelAPI
from src.backend.game.card import Card
from src.backend.game.constants import QUESTS, CARDS
from src.backend.game.person import PERSON
from src.backend.game.store import STORE
from src.backend.game.format_number import format_number

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
    return render_template(
        'game/index.html',
        max_xp = LevelAPI.get_xp_max_for_current_level(PERSON.xp),
        quests = QUESTS,
        format_number = format_number,
        PERSON = PERSON,
        STORE = STORE) 