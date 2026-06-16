from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

items = [{"name": "Mango"}, {"name": "Banana"}, {"name": "Durian"}]
items2 = {1: {"name": "Mango"},2:{"name": "Banana"},3:{"name": "Durian"}}

# Hello World home page
@app.route('/')
def hello_world():
    return 'Hello World'

# Get items in list
@app.route("/api/items", methods=["GET"])
def api_get_items():
    return jsonify(items)
    

@app.route("/items", methods=["GET"])
def get():
    return render_template("items.html",items=items)

# Get specific item in list
@app.route("/api/items/<string:item_name>", methods=["GET"])
def api_get_item(item_name):
    for item in items:
        if item["name"].lower() == item_name.lower():
            return jsonify(item)
    return jsonify({"error": "Item not found"}), 404
    #return render_template("items.html",items=items)
    
# Add item to a list
@app.route("/add", methods=["POST","GET"])
def add_item():
    if request.method == "POST":
        new_item = request.form["name"]
        items.append({"name": new_item})
        return redirect(url_for("get"))
    else:
        return render_template("add_item.html")

@app.route("/api/add", methods=["POST","GET"])
def api_add_item():
    print(request.get_json())
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Must include name"}), 400
    new_item = {"name": data["name"]}
    items.append(new_item)
    return jsonify(new_item), 201

# Remove item from a list
@app.route("/remove", methods=["POST","GET","DELETE"])
def remove_item():
    if request.method == "POST":
        new_item = request.form["name"].title()
        items.remove({"name": new_item})
        return redirect(url_for("get"))
    else:
        return render_template("delete_item.html")

@app.route("/api/remove/<string:item_name>", methods=["DELETE"])
def api_delete_item(item_name):
    for item in items:
        if item["name"].lower() == item_name.lower():
            items.remove(item)
            return jsonify({"message": "Item deleted" })
    return jsonify({"error": "Item not found"}), 404

# Update item in list
@app.route("/update", methods=["POST","GET","PUT"])
def update_item():
    if request.method == "POST":
        old_name = request.form["old_name"].title()
        new_name = request.form["new_name"].title()
        for item in items:
            if item["name"] == old_name:
                item["name"] = new_name
        return redirect(url_for("get"))
    return render_template("update_item.html")

@app.route("/api/update/<string:item_name>", methods=["PUT"])
def api_update_item(item_name):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Didn't receive JSON data"}), 400
    if "name" not in data:
        return jsonify({"error": "Name not found" }), 400
    for item in items:
        if item["name"].lower() == item_name.lower():
            item["name"] = data["name"]
            return jsonify({
                "message": "Item updated",
                "item": item})
    return jsonify({"error": "Item not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
