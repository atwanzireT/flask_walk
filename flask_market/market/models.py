from . import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False, unique = True)
    price = db.Column(db.Integer, nullable = False)
    barcode = db.Column(db.String(12), nullable = False, unique = True)
    description = db.Column(db.String, nullable = False)
    
    def __repr__(self) -> str:
        return f'Item: {self.name}'