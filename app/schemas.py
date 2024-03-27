from app.extensions import marshmallow as ma
from marshmallow import fields, pre_dump

class ProductSchema(ma.Schema):

    class Meta:
        include_relationships = True

    id = fields.Field()
    name = fields.Field()
    lote_number = fields.Field()
    validity_date = fields.DateTime()
    categorys = fields.Method("slugify_category")
    added_att = fields.DateTime()

    def slugify_category(self, data):
        return data.categorys[0].name

class ProductClosedExpSchema(ma.Schema):

    id = fields.Field()
    name = fields.Field()
    lote_number = fields.Field()
    validity_date = fields.DateTime()
    added_att = fields.DateTime()

    @pre_dump(pass_many=True)
    def sort_products_by_expiration_date(self, data, many):
        return sorted(data, key=lambda x: x.validity_date)

class ProductsLastAdded(ma.Schema):

    id = fields.Field()
    name = fields.Field()
    lote_number = fields.Field()
    validity_date = fields.DateTime()
    added_att = fields.DateTime()

    @pre_dump(pass_many=True)
    def sort_products_by_last_added_date(self, data, many):
        return sorted(data, key=lambda x: x.added_att)

class CategorySchema(ma.Schema):

    class Meta:
        include_relationships = True

    id = fields.Field()
    name = fields.Field()
    added_att = fields.DateTime()
    products = fields.Nested(ProductSchema, many=True)




