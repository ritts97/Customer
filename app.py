import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('Customer.pkl','rb'))
st.title("Customer Segmentation")

age = float(st.text_input("Enter Age: ","18"))
salary = float(st.text_input("Enter Salary: ","10000"))

featureInput = np.array([[age,salary]])

customerType = model.predict(featureInput)
customerTypeName

if customerType == [0]:
  customerTypeName == "Non Purchasing"
else:
  customerTypeName == "Purchasing"

st.write(f'*Hello!* :sunglasses: . Customer Group : {customerTypeName} ')
