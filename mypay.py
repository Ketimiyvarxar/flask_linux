from flask import Flask, render_template, request, redirect, url_for
#need for my database
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)   # Flask constructor 

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
db =SQLAlchemy(app)
class Prices(db.Model):

    country = db.Column(db.String(100),primary_key=True)
    price = db.Column(db.String(100), nullable=False)

class Low(db.Model):
    id = db.Column(db.String(200),primary_key=True)
    volume = db.Column(db.String(100), nullable=False)

class Mid(db.Model):
    id = db.Column(db.String(200),primary_key=True)
    volume = db.Column(db.String(100), nullable=False)

class High(db.Model):
    id = db.Column(db.String(200),primary_key=True)
    volume = db.Column(db.String(100), nullable=False)
  
# A decorator used to tell the application 
# which URL is associated function 
@app.route('/', methods=['post','GET'])       
def test(): 
    return render_template ('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    time = request.form.get('time')
    speed = request.form.get('speed')
    region = request.form.get('region')

    result = Prices.query.filter_by(country=region).first()
    if result:
        output = f"Price in {region} is {result.price}Euro for 1000 Liters.\n Take care of the planet and your wallet ;)"

    else:
        output = "No data found for the specified region.\n  Take care of the planet and your wallet ;)"

    return render_template('result.html', output=output)
  
if __name__=='__main__': 
   app.run(host='0.0.0.0',port=5000) 
