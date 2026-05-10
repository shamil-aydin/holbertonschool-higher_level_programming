#!/usr/bin/python3
"""Flask application that displays data from JSON or CSV files."""
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json():
    """Read and return data from products.json."""
    with open('products.json', 'r') as f:
        return json.load(f)


def read_csv():
    """Read and return data from products.csv."""
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products


@app.route('/products')
def products():
    """Render products page from JSON or CSV source."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    else:
        return render_template(
            'product_display.html', error="Wrong source")

    if product_id:
        data = [p for p in data if str(p['id']) == str(product_id)]
        if not data:
            return render_template(
                'product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
