from src.build_flask import *
from src.backend.common.fhandler import file_read
from yaml import safe_load
@app.route('/game',methods = [GET])
def game_index():
    with open('./src/xp_table.yml') as f:
        quests = safe_load(f)
    return render_template(
        'game/index.html',
        name= 'Test',
        level = 120,
        current_xp = 10,
        max_xp = 100,
        coin = 150,
        ruby = 10,
        quests = quests) 