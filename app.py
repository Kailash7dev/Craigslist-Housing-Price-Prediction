#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# from flask import Flask, render_template, request
# import jsonify
# import requests
# import pickle
# import numpy as np
# import sklearn
# from sklearn.preprocessing import StandardScaler
# app = Flask(__name__)
# model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
# @app.route('/',methods=['GET'])
# def Home():
#     return render_template('index.html')


# standard_to = StandardScaler()
# @app.route("/predict", methods=['POST'])
# def predict():
#     Fuel_Type_Diesel=0
#     if request.method == 'POST':
#         Year = int(request.form['Year'])
#         Present_Price=float(request.form['Present_Price'])
#         Kms_Driven=int(request.form['Kms_Driven'])
#         Kms_Driven2=np.log(Kms_Driven)
#         Owner=int(request.form['Owner'])
#         Fuel_Type_Petrol=request.form['Fuel_Type_Petrol']
#         if(Fuel_Type_Petrol=='Petrol'):
#                 Fuel_Type_Petrol=1
#                 Fuel_Type_Diesel=0
#         else:
#             Fuel_Type_Petrol=0
#             Fuel_Type_Diesel=1
#         Year=2020-Year
#         Seller_Type_Individual=request.form['Seller_Type_Individual']
#         if(Seller_Type_Individual=='Individual'):
#             Seller_Type_Individual=1
#         else:
#             Seller_Type_Individual=0	
#         Transmission_Mannual=request.form['Transmission_Mannual']
#         if(Transmission_Mannual=='Mannual'):
#             Transmission_Mannual=1
#         else:
#             Transmission_Mannual=0
#         prediction=model.predict([[Present_Price,Kms_Driven2,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual]])
#         output=round(prediction[0],2)
#         if output<0:
#             return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
#         else:
#             return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(output))
#     else:
#         return render_template('index.html')

# if __name__=="__main__":
#     app.run(debug=True)


# In[ ]:


from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)

# model = pickle.load(open('lin_reg.pkl', 'rb'))
# model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
with open('lin_reg5.pkl','rb') as f:
     model = pickle.load(f)

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


# standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    house_Type_condo = 0
    house_Type_duplex = 0
    house_Type_house = 0
    house_Type_townhouse=0
    house_Type_others=0
    house_Type_apartment=0
    parking_type_attached = 0
    parking_type_detached = 0
    parking_type_street = 0
    parking_type_no = 0
    if request.method == 'POST':
        bathroom = float(request.form['bathroom'])
        area=float(request.form['area'])
        bedroom=int(request.form['bedroom'])
        isFurnished =int(request.form['Finishing'])
#         Kms_Driven2=np.log(Kms_Driven)
#         Owner=int(request.form['Owner'])
        houseType = request.form['houseType']
        if(houseType=='House'):
            house_Type_house = 1
        elif(houseType=='Condo'):
            house_Type_condo = 1
        elif(houseType=='Apartment'):
            house_Type_apartment = 1
        elif(houseType=='Town House'):
            house_Type_townhouse = 1
        elif(houseType=='Duplex'):
            house_Type_duplex = 1
        elif(houseType=='others'):
            house_Type_others = 1
        else:
            pass
#         Year=2020-Year
        parkingType=request.form['parkingType']
        if(parkingType=='No Parking'):
            parking_type_no = 1
        elif(parkingType=='Attached Garage'):
            parking_type_attached = 1
        elif(parkingType=='Detached Garage'):
            parking_type_detached = 1
        elif(parkingType=='Street Parking'):
            parking_type_street = 1
        else:
            pass
#         Transmission_Mannual=request.form['Transmission_Mannual']
#         if(Transmission_Mannual=='Mannual'):
#             Transmission_Mannual=1
#         else:
#             Transmission_Mannual=0
        x=[bedroom,area,bathroom, isFurnished, house_Type_condo, house_Type_duplex, house_Type_house, house_Type_others,
          house_Type_townhouse, parking_type_detached, parking_type_no, parking_type_street]
        prediction=model.predict([x])
#         output=round(prediction[0],2)
        price = np.exp(prediction)
        if price<0:
            return render_template('index.html',prediction_texts="Housing Data provided is not valid")
        else:
            return render_template('index.html',prediction_text="You Can Buy/Sell the house at {}".format(price))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)


