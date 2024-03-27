from flask import Blueprint, request, jsonify
from datetime import datetime

from app.extensions import database
from app.schemas import ProductSchema, ProductClosedExpSchema, ProductsLastAdded

from app.models import Product

HomeRoute = Blueprint("HomeRoute", __name__, url_prefix="/")

@HomeRoute.route('', methods=["GET"])
def get_products():
    try:
        products_schema = ProductSchema(many=True)
        products = Product.query.all()
        return products_schema.dump(products)
    except Exception as exception:
        return jsonify({"error": True, "message": str(exception)}), 400

@HomeRoute.route('/get_closed_expiration', methods=['GET'])
def get_closed_expiration():
    try:
        products = Product.query.all()
        products = ProductClosedExpSchema(many=True).dump(products)

        return products

    except Exception as exception:
        return jsonify({"error": True, "message": str(exception)}), 400

@HomeRoute.route('/get_last_added', methods=['GET'])
def get_last_added():
    try:
        products = Product.query.all()
        products = ProductsLastAdded(many=True).dump(products)

        return products

    except Exception as exception:
        return jsonify({"error": True, "message": str(exception)}), 400



