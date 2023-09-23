from flask import Flask,request,render_template

import pickle
tree_model=pickle.load(open('E:\ML PROJECTS\TATA MOTORS PRICE PREDICTION\Models\TREE_MODEL.pkl','rb'))

application=Flask(__name__)

app=application

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/price',methods=["GET","POST"])
def price_predict():
    if request.method=='POST':
         
         OPEN=float(request.form.get("OPEN"))
         HIGH=float(request.form.get("HIGH"))
         LOW=float(request.form.get("LOW"))
         VOLUME=float(request.form.get("VOLUME"))
         YEAR=float(request.form.get("YEAR"))
         MONTH=float(request.form.get("MONTH"))
         DATE=float(request.form.get("DATE"))
         

         new_data=([[OPEN,HIGH,LOW,VOLUME,YEAR,MONTH,DATE]])
         result=tree_model.predict(new_data)
         
         return render_template('foam.html',result=result[0])
        
    else:
        return render_template('foam.html')


if __name__=="__main__":
    app.run(host='0.0.0.0')
    