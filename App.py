# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask,render_template,request,jsonify
import pickle
import numpy as np
import MySerial as my

model = pickle.load(open('model.pkl','rb'))

app = Flask(__name__)


@app.route('/')
def login():
    return render_template("login.html")

@app.route('/main')
def main():
    return render_template("index.html")

@app.route('/predict')
def pred():
    return render_template('main.html',prediction_text = "", data = my.dats)  
    

# @app.route('/take_me')
# def predict():
#     return render_template('main.html',prediction_text = "",data = my.dats)

@app.route('/predict',methods=['GET','POST'])
def prediction():
    print(request.form.values())
    n=request.form['nitrogen']
    phos=request.form['phosp']
    k=request.form['potts']
    pH=request.form['ph']
    m=request.form['moist']
    t=request.form['temp']
    features=list(map(float,[pH,n,phos,k,t,m]))

    print(features)
    final_features = [np.array(features)]
    #print(final_features)
    prediction = model.predict(final_features)
    print(prediction)
    if prediction == 0:
        return render_template('main.html', prediction_text = "Not Fertile",data = my.dats)
    elif prediction > 0:
        return render_template('main.html', prediction_text = "Fertile",data = my.dats)      

if __name__ == '__main__':
	app.run(debug=True)
