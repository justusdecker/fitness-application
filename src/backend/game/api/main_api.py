from src.build_flask import *
from src.backend.game.person import PERSON
class GameAPI:

    @app.route('/api/get')
    def api_get():
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