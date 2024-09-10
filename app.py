import pickle
from flask import Flask,request,render_template
# import numpy 
# import pandas
# from sklearn.preprocessing import StandardScaler

app= Flask(__name__)

##import model and standard scalar pickle
model=pickle.load(open(r'C:\Users\sowmy\Desktop\End Project\Model\trained_model.pkl','rb'))
scaler=pickle.load(open(r'C:\Users\sowmy\Desktop\End Project\Model\end_scaler.pkl','rb'))


@app.route('/',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='POST':
        temperature=float(request.form.get('temperature'))
        humidity=float(request.form.get('humidity'))
        moisture=float(request.form.get('moisture'))
        soilType=float(request.form.get('soilType'))
        cropType=float(request.form.get('cropType'))
        nitrogen=float(request.form.get('nitrogen'))
        potassium=float(request.form.get('potassium'))
        phosphorous=float(request.form.get('phosphorous'))
        #scaling the data
        new_scaled_data=scaler.transform([[temperature,humidity,moisture,soilType,cropType,nitrogen,potassium,phosphorous]])
        # predicting the fertilizer
        result=model.predict(new_scaled_data)
        
        ferti_dict={
            0:'10-26-26',
            1:'14-35-14',
            2:'17-17-17',
            3:'20-20',
            4:'28-28',
            5:'DAP',
            6:'Urea'}
        Result=ferti_dict.get(result[0])
        
    
        return render_template('Project.html',result=Result)

    else:
        return render_template('Project.html')
    from app import app

if __name__ == '__main__':
    app.run(debug=True)
