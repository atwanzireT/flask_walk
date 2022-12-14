from . import app, render_template, db, redirect, url_for
from .models import Item, User
from .forms import RegisterForm



@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/market/')
def market():
    items = Item.query.all()
    return render_template('market.html', items=items)


@app.route('/user/')
def users():
    users = User.query.all()
    return users


@app.route('/register/', methods = ['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email=form.email.data,
                              password_hash=form.password1.data,
                              )
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market'))
    if form.errors != {}: # if there are not errors from the validation
        for err_msg in form.errors.values():
            print(f"There was an error: {err_msg}", category = 'danger')
    return render_template('register.html', form=form)


# @app.route('/database_user')
# def database():
#     users = [
#         {"username":"Tom", "email":"tom@gmail.com", "password_hash":"1234"},
#         {"username":"John", "email":"john@gmail.com", "password_hash":"1234"},
#         {"username":"Janet", "email":"janet@gmail.com", "password_hash":"1234"},

#     ]
#     for user in users:
#         user = User(username=user['username'], email=user['email'], password_hash=user['password_hash'])
#         db.session.add(user)
#         db.session.commit()
#     return "Thank you!"

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