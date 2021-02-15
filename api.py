import flask
from flask import request, jsonify
import json
from books import allBooks

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])

def home():
    return "<h1>My first Python API</h1>"

@app.route('/books', methods=['GET'])
def books():
    books = allBooks
    results = []
    if 'id' in request.args:
        id = int(request.args['id'])
        print(f'id {id} found in args')
        for book in books:
            if book['id'] == id:
                print(f"Found book with id {book['id']}")
                results.append(book)
    else:
        results.extend(allBooks)

    if len(results) == 0:
        return "<h1>404</h1><p>The resource could not be found.</p>", 404
    return jsonify(results)

app.run()
