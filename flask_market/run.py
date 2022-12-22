from market import app, db

with app.app_context():
    db.create_all()
    # db.drop_all()

if __name__ == "__main__":
    app.run(debug=True)