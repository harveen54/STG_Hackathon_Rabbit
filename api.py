#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

items = [
    {
        'id': 1,
        'address_1': u'images/1.jpg',
		'address_2': u'images/2.jpg',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'address_1': u'images/2.jpg',
		'address_2': u'images/1.jpg',
        'description': u'Cold Storage', 
        'done': False
    }
]

@app.route('/stg/items', methods=['GET'])
def get_items():
    return jsonify({'items': items})

@app.route('/stg/items/<int:id>', methods=['GET'])
def selected_item(id):
	local_item = [item for item in items if item['id'] == id]
	if len(local_item) == 0:
		abort(404)
	return jsonify({'item': local_item[0]})
	
	
if __name__ == '__main__':
    app.run(debug=True)