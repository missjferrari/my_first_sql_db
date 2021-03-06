from flask import Flask, render_template
from flask import SQLAlchemy
from datetime import datetime

app = Flask("app")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///villain.db"

db = SQLAlchemy(app)

class Villain(db.Model)
  id = db.Column(db.Integer, primary_key= True)
  name = db.Column(db.String(80), unique=True, nullable=False)
  description = db.Column(db.String(250), nullable=False)
  interests = db.Column(db.String(250), nullable=False)
  url = db.Column(db.String(250), nullable=False)
  date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

db.create_all()
db.session.commit()

def _repr_(self):
  return "<Villain " + self.name + ">"

@app.route("/")
def villains_cards():
  return render_template("villain.html")

app.run(host='0.0.0.0', port=8080)