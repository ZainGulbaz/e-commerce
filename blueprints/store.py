from flask_smorest import Blueprint,abort;
from flask.views import MethodView;
from schemas.store import StoreSchema; 
from db import db;
from models import store_model;
from commons import CustomError;



blp = Blueprint("stores",__name__,"Create,Update,Delete and Get Stores");

@blp.route("/store/<string:storeId>")
class Store(MethodView):
    @blp.response(200,StoreSchema)
    def get(self,storeId):
        try:
            store= store_model.query.get(storeId);
            print("Store---------------",store);
            if(store==None):
                raise CustomError("The requested store does not exist","not_found_error");
            return store.to_json();
        except Exception as error:
            if(error.name=="not_found_error"):
                abort(404,message=error.message);
            abort(400,message="The stores cannot be accessed");




@blp.route("/store")
class Stores(MethodView):

    @blp.arguments(StoreSchema)
    @blp.response(201,StoreSchema)
    def post(self,body):
        store=store_model(**body);
        try:
            db.session.add(store);
            db.session.commit();
            return store.to_json();
        except Exception as error:
            if(error.__class__.__name__=="IntegrityError"):
                abort(404,message=error.orig.args[1]);
            abort(200,"The store cannot be created successfully");    
        
