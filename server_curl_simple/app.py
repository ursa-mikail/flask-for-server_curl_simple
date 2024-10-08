from flask import Flask, request, jsonify

app = Flask(__name__)

items = {}

@app.route('/items/<item_id>', methods=['GET'])
def get_item(item_id):
    if item_id in items:
        return jsonify(items[item_id]), 200
    else:
        return jsonify({"error": "Item not found"}), 404

@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    item_id = data['item_id']
    items[item_id] = data
    return jsonify({"message": "Item created"}), 201

@app.route('/items/<item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    if item_id in items:
        items[item_id] = data
        return jsonify({"message": "Item updated"}), 200
    else:
        return jsonify({"error": "Item not found"}), 404

@app.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id in items:
        del items[item_id]
        return jsonify({"message": "Item deleted"}), 200
    else:
        return jsonify({"error": "Item not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
