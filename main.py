from flask import Flask, jsonify, request
from ArXivService import ArXivService

app = Flask(__name__)

arXivService = ArXivService()

@app.route('/api/search', methods=['GET'])
def search():
    search_query = request.args.get('search_query')
    start = request.args.get('start')
    max_results = request.args.get('max_results')
    search_results = arXivService.get_search_results(search_query, start, max_results)
    return jsonify(search_results)