from flask import Blueprint

dire = Blueprint('dire', __name__)


@dire.route('/getdire', methods=['GET'])
def getdire():
    return {'key': 'Directivos'}
