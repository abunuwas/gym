import datetime

from flask import jsonify, request

from app import app


@app.before_request
def before_request():
    g.data = request.get_json() or request.values()


@app.route('/')
def index():
    return 'hey'


@app.route('/sets', methods=['GET'])
def sets_get():
    date = datetime.datetime.utcnow()
    return jsonify([
        {
            'date': datetime.datetime.isoformat(date),
            'exercise': 'Bench Press',
            'repetitions': 10,
            'weight': 20,
            'weight_unit': 'kg',
            'performance': 'good'
        }
    ])


@app.route('/set/<int:id>', methods=['GET'])
def set_get(id):
    date = datetime.datetime.utcnow()
    return jsonify([
        {
            'date': datetime.datetime.isoformat(date),
            'exercise': 'Bench Press',
            'repetitions': 10,
            'weight': 20,
            'weight_unit': 'kg',
            'performance': 'good'
        }
    ])


@app.route('/set', methods=['POST'])
def set_post():
    data = g.data


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
