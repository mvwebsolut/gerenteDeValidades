from datetime import datetime

from app.extensions import database as db

categorys_products = db.Table('category_products',
    db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('categorys.id'), primary_key=True)
)

class Categorys(db.Model):

    __tablename__ = "categorys"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    products = db.relationship("Product", back_populates="categorys", secondary="category_products")
    added_att = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def __repr__(self):
        return f'<Category id={self.id} name="{self.name}" added_att="{self.added_att}">'

