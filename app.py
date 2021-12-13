#Importing the libraries
import pickle
from flask import Flask, render_template, request

#Global Variables
app = Flask(__name__)
loadedModel = pickle.load(open('Model.pkl', 'rb'))

#Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prediction', methods=['POST'])
def prediction():
    Temp_C = request.form['Temp_C']
    DewPointTemp_C= request.form['DewPointTemp_C']	
    RelHum=request.form['RelHum']
    WindSpeed_km=request.form['WindSpeed_km']
    Visibility_km=request.form['Visibility_km']	
    Press_kPa=request.form['press_kPa'] 

    prediction = loadedModel.predict([[Temp_C, DewPointTemp_C, RelHum, WindSpeed_km,Visibility_km, Press_kPa]])[0]

    return render_template('index.html', api_output=prediction)
   

#Main function
if __name__ == '__main__':
    app.run(debug=True)