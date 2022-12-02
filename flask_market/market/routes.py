from . import app, render_template, db
from .models import Item


@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/market/')
def market():
    items = Item.query.all()
    return render_template('market.html', items = items)

# @app.route('/database')
# def database():
#     items = [
#         {"name":"techno", "price":189, "barcode":"346782128", "description":"so cool"},
#         {"name":"oppo", "price":289, "barcode":"343422128", "description":"so cool"},
#         {"name":"redmi", "price":189, "barcode":"346782441", "description":"so cool"},
#         {"name":"LG", "price":189, "barcode":"346782098", "description":"so cool"},
#     ]
#     for item in items:
#         item = Item(name=item['name'], price=item['price'], barcode=item['barcode'], description=item['description'])
#         db.session.add(item)
#         db.session.commit()
#     return "Thank you!"