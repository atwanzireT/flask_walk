from flask_sqlalchemy import SQLAlchemy
from models.models import *
from views import views

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
# db = SQLAlchemy(app)
from flask import Flask, render_template, request

app = Flask(__name__)

# create model
class Posts(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), nullable = False)
    body = db.Column(db.String(500))
    created = db.Column(db.DateTime, default = datetime.utcnow())


    def __repr__(self):
        return '<Title %r>' % self.title
        
@app.route('/')
def index():
    title = "Fedora's Blog"
    names = ['tim', 'tom', 'tonny']
    return render_template('index.html', title = title, names = names)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/subcribe/')
def subcribe():
    return render_template('subcribe.html')

@app.route('/form/', methods = ['POST'])
def form():
    email = request.form.get('email')
    name = request.form.get('name')
    message = "Thank you for subcribing to our newsletter."
    if not email or not name:
        error_statement = "All fields required ..."
        return render_template("fail.html", error_statement = error_statement)

    return render_template('form.html', name = name)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)