from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from ArXivService import ArXivService

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

arXivService = ArXivService()

@app.route('/api/search', methods=['GET'])
@cross_origin()
def search():
    search_query = request.args.get('search_query')
    start = request.args.get('start')
    max_results = request.args.get('max_results')
    search_results = arXivService.get_search_results(search_query, start, max_results)
    return jsonify(search_results)