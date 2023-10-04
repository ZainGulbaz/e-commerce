from db import db;

class store_model(db.Model):
    id=db.Column(db.Integer,primary_key=True);
    name=db.Column(db.String(80),unique=True,nullable=False);


    def to_json(self):
        return{
            "id":self.id,
             "name":self.name
        }

