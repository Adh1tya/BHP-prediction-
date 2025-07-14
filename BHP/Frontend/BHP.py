import streamlit as st
from PIL import Image
import pickle
import numpy as np

model = pickle.load(open('../Model/ML_Model_LanPRed_01.pkl', 'rb'))

def run():
    img1 = Image.open('bank.png')
    img1 = img1.resize((156,145))
    st.image(img1,use_column_width=False)
    st.title("BHP Price Prediction")


    loc_display = ('Bommanahalli','Electronics City','Indira Nagar','Vijayanagar', 'Whitefield')
    loc_options = list(range(len(loc_display)))
    location = st.selectbox("location",loc_options, format_func=lambda x: loc_display[x])

    bed = st.number_input("Number of Bedrooms required",value=0.0)


    
    sqrt = st.number_input("House Area in sqft",value=0.0)    
    
    
      

   
    bath = st.number_input("Number of Bathrooms required",value=0.0)  

    
    balcony = st.number_input("Number of Balconies required",value=0) 

    
    
    if st.button("Submit"):
        
        features = [[location , bed, sqrt, bath ,balcony]]
        print(features)
        
        Profit = model.predict(features)
        st.subheader('Predictied Price in lakhs :')
        st.subheader('INR'+' '+str(np.round(Profit[0])))

run()