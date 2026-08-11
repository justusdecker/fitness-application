from src.build_flask import *
from time import time
from src.backend.game.person import PERSON
from src.backend.game.constants import QUESTS
from src.backend.game.level_calculations import LevelAPI
class GameAPI:

    @app.route('/api/quest_solve/<key>')
    def api_quest_solve(key: str):
        PERSON.xp += QUESTS[key]['xp']
        PERSON.coin += QUESTS[key]['coin'] if 'coin' in QUESTS[key] else 0
        PERSON.material += QUESTS[key]['material'] if 'material' in QUESTS[key] else 0
        PERSON.history.add(int(time()*1000), key)
        PERSON.save()
        return "", 200
    @app.route('/api/get')
    def api_get():
        return jsonify(
            {
                'coin': PERSON.formattedCoin,
                'material': PERSON.formattedMaterial,
                'xp': PERSON.xp,
                'fxp': PERSON.formattedXP,
                'level': PERSON.level,
                'xp_max': PERSON.formattedXPMax,
                'xp_percentage': PERSON.xpPercentage
            }
        )
    @app.route('/api/increase')
    def api_increase():
        data = request.args.get('data')
        if data is None: raise NotImplementedError()
        inc = int(((PERSON.level * 2) + ((PERSON.level // 10) * 10) + 1))
        PERSON.coin += inc
        print(F'{inc}📀')
        PERSON.save()
        return "", 200