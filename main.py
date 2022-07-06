from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.users import Userregister
from resources.item import Itemlist, Item
from resources.store import StoreList, Store

from db import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'F*ckNMHH'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Itemlist, '/items')
api.add_resource(Userregister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/storelist')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
