from flask import Flask, render_template

app = Flask(__name__)

newletters = [
    {'email':'kusa@gmail.com', 'name':'Kusa'},
]

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