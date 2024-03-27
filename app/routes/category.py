from flask import Blueprint, request, jsonify
from datetime import datetime

from app.extensions import database
from app.schemas import CategorySchema

from app.models import Categorys

CategoryRoute = Blueprint("CategoryRoute", __name__, url_prefix="/categorys")

@CategoryRoute.route('', methods=["GET"])
def get_categorys():
    try:
        category_schema = CategorySchema(many=True)
        categorys = Categorys.query.all()
        return category_schema.dump(categorys)
    except Exception as exception:
        return jsonify({"error": True, "message": str(exception)}), 400

@CategoryRoute.route("/add", methods=["POST"])
def add_category():
    try:
        payload = request.json

        if Categorys.query.filter_by(name=payload['name']).first():
            raise Exception("categoria já foi cadastrada.")

        new_category = Categorys(
            name=payload['name'],
            added_att=datetime.now()
        )
        database.session.add(new_category)
        database.session.commit()

        category_schema = CategorySchema()

        return category_schema.dump(new_category)

    except Exception as exception:
        return jsonify({"error": True, "message": str(exception)}), 400

@CategoryRoute.route('/delete', methods=['DELETE'])
def delete_category():
    try:
        payload = request.json

        category = Categorys.query.filter_by(id=payload['category_id']).first()
        if not category:
            raise Exception("Categoria não encontrado")

        database.session.delete(category)
        database.session.commit()

        return jsonify({"error": False, "message": f"Categoria {category.name} deletado com sucesso"}), 200

    except Exception as exception:
        return jsonify({"error": True, "message": str(exception)}), 400