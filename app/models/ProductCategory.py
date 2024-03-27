from app.extensions import database as db


class product_category(db.Model):

    __tablename__ = "product_category"

    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey("categorys.id"))
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))







