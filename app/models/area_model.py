from app import db

class Area(db.Model):
    __tablename__ = "area"
    #id = db.Column(type,key,auto)
    id = db.Column(db.Integer,primary_key=True,auto_increment=True)
    nome = db.Column(db.String(200))