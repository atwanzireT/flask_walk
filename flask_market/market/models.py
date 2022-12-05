from . import db

class User(db.Model):
    id = db.Column(db.integer, primary_key = True)
    username = db.Column(db.String, nullable = False, unique = True)
    email = db.Column(db.String, nullable = False, unique = True)
    password_hash = db.Column(db.String, nullable = False)
    budget = db.Column(db.Integer, nullable = False, unique = True, default = 1000)
    items = db.relationship('Item', backref = 'owned_user', lazy = True)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False, unique = True)
    price = db.Column(db.Integer, nullable = False)
    barcode = db.Column(db.String(12), nullable = False, unique = True)
    description = db.Column(db.String, nullable = False)
    owner = db.column(db.integer, db.Foreignkey('user.id'))
    
    def __repr__(self) -> str:
        return f'Item: {self.name}'