from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price", type=float, required=True, help="this field can't be blank")
    parser.add_argument("store_id", type=int, required=True, help="Every item needs a store...")

    @jwt_required()
    def get(self, name):
        item = ItemModel.get_by_name(name)
        if item:
            return item.json(), 200
        else:
            return {"message": "not found"}, 404

    def post(self, name):
        item = ItemModel.get_by_name(name)
        if item:
            return {'message': "item with name '{}' already exists".format(name)}, 400
        else:
            data = Item.parser.parse_args()
            _item = ItemModel(name, data['price'], data['store_id'])
            try:
                _item.save_to_db()
            except:
                return {"message": "An error occurred during insertion"}, 500
            return _item.json(), 201

    @jwt_required()
    def delete(self, name):
        _item = ItemModel.get_by_name(name)
        if _item:
            _item.delete_from_db()

        return {"message": "Item deleted"}, 201

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.get_by_name(name)
        if item:
            item.price = data['price']
        else:
            item = ItemModel(name, data['price'], data['store_id'])
        item.save_to_db()


class Itemlist(Resource):
    def get(self):
        return {"items": [_item.json() for _item in ItemModel.query.all()]}
