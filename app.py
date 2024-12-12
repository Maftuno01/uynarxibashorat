import streamlit as st
import joblib
import numpy as np
#uzgarish
# Modelni yuklash
model = joblib.load('housemodel.pkl')

# Streamlit interfeysi
st.title("Uy Narxini Bashorat Qilish")

# Foydalanuvchidan ma'lumotlarni olish
length = st.slider("G'arbga uzoqlik (km)", 0, 100, 50)
width = st.slider("Shimolga uzoqlik (km)", 0, 100, 50)
median_age = st.slider("O'rtacha uy yoshi (yil)", 0, 50, 25)
total_rooms = st.slider("Xonalar soni", 1, 10, 5)
total_bedrooms = st.slider("Yotoq xonalarining soni", 1, 5, 3)
population = st.slider("Aholi soni", 50, 1000, 500)

# Bashorat qilish tugmasi
if st.button("Narxni Bashorat Qiling"):
    # Foydalanuvchi parametrlari asosida modelni ishga tushurish
    input_data = np.array([[length, width, median_age, total_rooms, total_bedrooms, population]])
    
    # Model yordamida narxni bashorat qilish
    predicted_price = model.predict(input_data)
    
    # Bashoratni foydalanuvchiga ko'rsatish
    st.success(f"Bashorat qilingan uy narxi: {predicted_price[0]:,.2f} dollar")





# import streamlit as st
# import joblib
# import numpy as np

# # Modelni yuklash
# model = joblib.load('housemodel.pkl')

# # Foydalanuvchidan ma'lumotlarni olish
# st.title("Uy Narxini Bashorat qilish")

# length = st.slider("G'arbga uzoqlik (km)", 0, 100, 50)
# width = st.slider("Shimolga uzoqlik (km)", 0, 100, 50)
# median_age = st.slider("O'rtacha uy yoshi (yil)", 0, 50, 25)
# total_rooms = st.slider("Xonalar soni", 1, 10, 5)
# total_bedrooms = st.slider("Yotoq xonalarining soni", 1, 5, 3)
# population = st.slider("Aholi soni", 50, 1000, 500)

# # Foydalanuvchi parametrlari asosida modelni ishga tushurish
# input_data = np.array([[length, width, median_age, total_rooms, total_bedrooms, population]])

# # Model yordamida narxni bashorat qilish
# predicted_price = model.predict(input_data)

# # Bashoratni foydalanuvchiga ko'rsatish
# st.write(f"Bashorat qilingan uy narxi: {predicted_price[0]:,.2f} dollar")


