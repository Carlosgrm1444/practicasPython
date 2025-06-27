from flask import Flask, jsonify

app = Flask(__name__)

from products import products


@app.route("/ping")
def ping():
    return jsonify({"message": "pong!"})


@app.route("/products")
def getProducts():
    return jsonify(products)


@app.route("/products/<string:product_name>")
def getProduct(product_name):
    productsFound = [product for product in products if product["name"] == product_name]
    if len(productsFound) > 0:
        return jsonify(productsFound[0])
    return "Product not found"


if __name__ == "__main__":
    app.run(debug=True, port=4000)
