from flask import Flask,render_template,request
import pickle
import numpy as np

app1 = Flask(__name__)
segment_model = pickle.load(open('knn_model.pkl','rb'))
@app1.route('/')
def index():
    return render_template('index.html')

@app1.route('/predict', methods =['POST'])
def predict_segment():
    Gender = int(request.form.get('Gender'))
    Ever_Married = int(request.form.get('Ever_Married'))
    Age = int(request.form.get('Age'))
    Profession = int(request.form.get('Profession'))
    Work_Experience = int(request.form.get('Work_Experience'))
    Spending_Score = int(request.form.get('Spending_Score'))
    Family_Size = int(request.form.get('Family_Size'))
    # prediction going on
    result = segment_model.predict(np.array([Gender, Ever_Married, Age, Profession, Work_Experience, Spending_Score, Family_Size]).reshape(1, 7))

    if result[0] == 1:
        result = 'SEGMENT A'
    elif result[0] == 2:
        result = 'SEGMENT B'
    elif result[0] == 3:
        result = 'SEGMENT C'
    else:
        result = 'SEGMENT D'

    return render_template('index.html',result = result)

if __name__ == '__main__':
    app1.run(debug=True)