import psycopg2
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://fnqeombzqtgudp:ebd41dae349d72b1c1c89c0b7b7f411c622e0cec55afd1ba0462b9cef5eb58f4@ec2-46-137-177-160.eu-west-1.compute.amazonaws.com:5432/ded8pkf75oa6nk'

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
