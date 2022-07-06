from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.get_by_name(name)
        if store:
            return store.json(), 200
        else:
            return {"message": "no store with that name"}, 404

    def post(self, name):
        store = StoreModel.get_by_name(name)
        if store:
            return {"message": "store with name {} already exists".format(name)}, 400
        else:
            store = StoreModel(name)
            try:
                store.save_to_db()
                return {"message": "store {} created".format(name)}, 201
            except:
                return {"message": "error writing to database"}, 500

    def delete(self, name):
        store = StoreModel.get_by_name(name)
        if store:
            store.delete_from_db()
            return {"message": "store {} deleted".format(name)}, 201
        else:
            return {"message": "no store with that name"}, 404


class StoreList(Resource):
    def get(self):
        return {"stores": [store.json() for store in StoreModel.query.all()]}

