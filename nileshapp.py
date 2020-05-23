import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('nilesh.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    
    int_data=[int(x) for x in request.form.values()]
    final_data=[np.array(int_data)]
    prediction=model.predict(final_data)
    
    output=round(prediction[0],2)
    
    return render_template('index.html',prediction_text='Employee salary should be $ {}'.format(output))




if __name__ == "__main__":
    app.run(debug=True)