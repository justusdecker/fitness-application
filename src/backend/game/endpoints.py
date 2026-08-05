from src.build_flask import *
from src.backend.common.fhandler import file_read
from yaml import safe_load
from src.backend.game.person import Person
from time import time
with open('./src/xp_table.yml', encoding='utf-8') as f:
    QUESTS = safe_load(f)
        
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
    PERSON.history.add(int(time()*1000), key)
    PERSON.save()
    return redirect('/game')

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
        ruby = PERSON.ruby,
        quests = QUESTS,
        xp_bar_fill = xpbf,
        history_count = PERSON.history.count()) 