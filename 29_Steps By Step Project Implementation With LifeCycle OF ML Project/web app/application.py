from flask import Flask, request, jsonify, render_template
import pickle
import numpy
import pandas as pd
from sklearn.preprocessing import StandardScaler


application = Flask(__name__)
app = application

# import ridge regressor and standard scaler pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

linreg_path = os.path.join(BASE_DIR, 'models', 'linreg.pkl')
scaler_path = os.path.join(BASE_DIR, 'models', 'scaler.pkl')

linreg=''
scaler=''

with open(linreg_path, 'rb') as f:
    linreg = pickle.load(f)

with open(scaler_path, 'rb') as f:
    scaler = pickle.load(f)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/predictdata', methods = ['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        try:
            Temprature = float(request.form.get('Temperature'))
            RH  = float(request.form.get('RH'))
            Ws = float(request.form.get('Ws'))
            Rain = float(request.form.get('Rain'))
            FFMC = float(request.form.get('FFMC'))
            DMC = float(request.form.get('DMC'))
            ISI = float(request.form.get('ISI'))
            Classes = float(request.form.get('Classes'))
            Region = float(request.form.get('Region'))


            df = pd.DataFrame(
                [[Temprature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]],
                columns=['Temperature', 'RH', 'Ws', 'Rain', 'FFMC', 'DMC', 'ISI', 'Classes', 'Region']
            )
            print('\n','='*60,'\n')
            print('Without Scaled:\n', df)
            new_data_scaled = scaler.transform(df)
            dict_data = df.to_dict(orient='records')[0]
            print('Data After Scaled:\n', new_data_scaled)

            print("Dict Data\n",dict_data)
            print('\n','='*60,'\n')

            result = linreg.predict(new_data_scaled)

        except Exception as e:
            result = [f'Error: {e}']
            dict_data = dict()


        return render_template(
            'home.html',
            result=result[0],
            data = dict_data
        )
    else:
        return render_template('home.html', data=None)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)