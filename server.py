import psycopg2
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://victors:victor77@localhost/DataCollector'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Data(db.Model):

    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key = True)
    weight = db.Column(db.Integer)
    height = db.Column(db.Integer)
    shoesize = db.Column(db.Integer)
    sex = db.Column(db.String)

    def __init__(self, height, weight, shoesize, sex):
        self.height = height
        self.weight = weight
        self.shoesize = shoesize
        self.sex = sex


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/success', methods=['POST'])
def success():
    
    if (request.method == 'POST'):
        height_ = request.form["height"]
        weight_ = request.form["weight"]
        shoesize_ = request.form["shoesize"]
        sex_ = request.form["sex"]
        data = Data(height_, weight_, shoesize_, sex_)
        db.session.add(data)
        db.session.commit()

        return render_template('success.html')


if __name__ == "__main__":
    app.run(debug=True)
