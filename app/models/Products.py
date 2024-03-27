from datetime import datetime

from app.extensions import database as db

class Product(db.Model):

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    lote_number = db.Column(db.String(255), nullable=False)
    validity_date = db.Column(db.DateTime, nullable=False)
    categorys = db.relationship("Categorys", back_populates="products", secondary="category_products")
    added_att = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def __repr__(self):
        return f'<Produto name="{self.name}" lote_number="{self.lote_number}" validity_date="{self.validity_date}" >'

