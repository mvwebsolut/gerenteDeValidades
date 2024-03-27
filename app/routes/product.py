from flask import Blueprint, request, jsonify
from datetime import datetime

from app.extensions import database
from app.utils.validators import validate_product
from app.schemas import ProductSchema

from app.models import Product, Categorys

ProductRoute = Blueprint("AddProduct", __name__, url_prefix="/products")

@ProductRoute.route('/', methods=["GET"])
def get_products():
    try:
        products_schema = ProductSchema(many=True)
        products = Product.query.all()
        return products_schema.dump(products)
    except Exception as exception:
        return jsonify({"error": True, "message": str(exception)}), 400

@ProductRoute.route('/delete', methods=['DELETE'])
def delete_product():
    try:
        payload = request.json

        product = Product.query.filter_by(id=payload['product_id']).first()
        if not product:
            raise Exception("Produto não encontrado")

        database.session.delete(product)
        database.session.commit()

        return jsonify({"error": False, "message": f"Produto {product.name} deletado com sucesso"}), 200

    except Exception as exception:
        return jsonify({"error": True, "message": str(exception)}), 400

@ProductRoute.route("/add", methods=["POST"])
def add_product():
    try:
        product = request.json
        validate_product(product)

        if Product.query.filter_by(lote_number=product['lote_number']).first():
            raise Exception("produto já foi cadastrado.")

        try:
            category = Categorys.query.filter_by(name=product['category_name']).first()
            if not category:
                category = Categorys(name=product['category_name'])
        except KeyError:
            category = Categorys.query.filter_by(name="sem categoria").first()
            if not category:
                category = Categorys(name="sem categoria")

        new_product = Product(
            name=product['name'],
            lote_number=product['lote_number'],
            validity_date=datetime.strptime(product['validity_date'], "%d/%m/%Y")
        )
        new_product.categorys.append(category)
        database.session.add(new_product)
        database.session.commit()

        product_schema = ProductSchema()

        return product_schema.dump(new_product)

    except Exception as exception:
        return jsonify({"error": True, "message": str(exception)}), 400






