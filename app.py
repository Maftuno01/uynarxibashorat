import streamlit as st
import pandas as pd
import joblib

# Modelni yuklash
model_filename = 'uynarxi.pkl'
model = joblib.load(model_filename)

# Sahifa sozlamalari
st.title("Uy narxini bashorat qilish")
st.write("Iltimos, uy haqidagi ma'lumotlarni kiriting va narxini bashorat qiling.")

# Kirish ma'lumotlari
uploaded_file = st.file_uploader("CSV faylni yuklang", type=["csv"])

if uploaded_file is not None:
    # Yuklangan faylni o'qish
    data = pd.read_csv(uploaded_file)

    # X ma'lumotlarini tayyorlash
    X = pd.get_dummies(data, drop_first=True)

    # Bashorat qilish
    predictions = model.predict(X)
    
    # Natijalarni chiqarish
    st.write("Bashorat qilingan narxlar:")
    result = pd.DataFrame({"Bashorat qilingan narx": predictions})
    st.write(result)

    # Natijalarni yuklab olish uchun tugma
    csv = result.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Natijalarni CSV formatida yuklab olish",
        data=csv,
        file_name='bashorat_qilingan_narxlar.csv',
        mime='text/csv',
    )
else:
    st.write("Iltimos, CSV faylni yuklang.")



# import streamlit as st
# import joblib
# import numpy as np
# #uzgarish
# # Modelni yuklash
# model = joblib.load('housemodel.pkl')

# # Streamlit interfeysi
# st.title("Uy Narxini Bashorat Qilish")

# # Foydalanuvchidan ma'lumotlarni olish
# length = st.slider("G'arbga uzoqlik (km)", 0, 100, 50)
# width = st.slider("Shimolga uzoqlik (km)", 0, 100, 50)
# median_age = st.slider("O'rtacha uy yoshi (yil)", 0, 50, 25)
# total_rooms = st.slider("Xonalar soni", 1, 10, 5)
# total_bedrooms = st.slider("Yotoq xonalarining soni", 1, 5, 3)
# population = st.slider("Aholi soni", 50, 1000, 500)

# # Bashorat qilish tugmasi
# if st.button("Narxni Bashorat Qiling"):
#     # Foydalanuvchi parametrlari asosida modelni ishga tushurish
#     input_data = np.array([[length, width, median_age, total_rooms, total_bedrooms, population]])
    
#     # Model yordamida narxni bashorat qilish
#     predicted_price = model.predict(input_data)
    
#     # Bashoratni foydalanuvchiga ko'rsatish
#     st.success(f"Bashorat qilingan uy narxi: {predicted_price[0]:,.2f} dollar")





# # import streamlit as st
# # import joblib
# # import numpy as np

# # # Modelni yuklash
# # model = joblib.load('housemodel.pkl')

# # # Foydalanuvchidan ma'lumotlarni olish
# # st.title("Uy Narxini Bashorat qilish")

# # length = st.slider("G'arbga uzoqlik (km)", 0, 100, 50)
# # width = st.slider("Shimolga uzoqlik (km)", 0, 100, 50)
# # median_age = st.slider("O'rtacha uy yoshi (yil)", 0, 50, 25)
# # total_rooms = st.slider("Xonalar soni", 1, 10, 5)
# # total_bedrooms = st.slider("Yotoq xonalarining soni", 1, 5, 3)
# # population = st.slider("Aholi soni", 50, 1000, 500)

# # # Foydalanuvchi parametrlari asosida modelni ishga tushurish
# # input_data = np.array([[length, width, median_age, total_rooms, total_bedrooms, population]])

# # # Model yordamida narxni bashorat qilish
# # predicted_price = model.predict(input_data)

# # # Bashoratni foydalanuvchiga ko'rsatish
# # st.write(f"Bashorat qilingan uy narxi: {predicted_price[0]:,.2f} dollar")


