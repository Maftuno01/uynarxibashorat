import streamlit as st
import pandas as np
import joblib

# Modelni yuklash
model_filename = 'uynarxi_randomforest.pkl'
model = joblib.load(model_filename)

# Sahifa sozlamalari
st.title("Uy narxini bashorat qilish")
st.write("Iltimos, uy haqidagi ma'lumotlarni kiriting va narxini bashorat qiling.")

# Tumanga oid narx diapazonlari
price_ranges = {
    'Bektemir': (19000, 29462.5, 40000),
    'Chilonzor': (12000, 47606.42, 644000),
    'Mirobod': (10500, 97400.88, 800000),
    'Mirzo Ulugbek': (10500, 57081.38, 504000),
    'Olmzor': (15500, 52045.55, 330000),
    'Sergeli': (13500, 43673.18, 120000),
    'Shayhontohur': (21000, 69446.2, 260000),
    'Uchtepa': (12300, 44558.04, 126000),
    'Yakkasaroy': (14500, 69535.19, 420000),
    'Yangihayot': (23000, 37000, 61900),
    'Yashnobod': (10500, 50671.55, 300000),
    'Yunusobod': (12500, 62552.72, 425600)
}

districts = list(price_ranges.keys())

# Foydalanuvchi kirishlari
selected_district = st.selectbox("Tumanni tanlang", districts)
if selected_district in price_ranges:
    min_price, mean_price, max_price = price_ranges[selected_district]
    st.write(f"{selected_district} uchun narxlar diapazoni: Min: {min_price}, O'rtacha: {mean_price}, Max: {max_price}")

size = st.number_input("Maydoni (m²)", min_value=1.0, step=1.0)

# Bashorat qilish tugmasi
if st.button("Narxni bashorat qilish"):
    # Foydalanuvchi kiritgan ma'lumotlardan massiv yaratish
    user_data = {
        'size': [size]
    }

    # Bashorat qilish
    prediction = model.predict(pd.DataFrame(user_data))[0]

    # Natijani chiqarish
    st.write(f"Bashorat qilingan uy narxi: {prediction:.2f}")

# import streamlit as st
# import pandas as pd
# import numpy as np
# import joblib

# # Modelni yuklash
# model_filename = 'uynarxi_randomforest.pkl'
# model = joblib.load(model_filename)

# # Sahifa sozlamalari
# st.title("Uy narxini bashorat qilish")
# st.write("Iltimos, uy haqidagi ma'lumotlarni kiriting va narxini bashorat qiling.")

# # Tumanga oid narx diapazonlari
# price_ranges = {
#     'Bektemir': (19000, 29462.5, 40000),
#     'Chilonzor': (12000, 47606.42, 644000),
#     'Mirobod': (10500, 97400.88, 800000),
#     'Mirzo Ulugbek': (10500, 57081.38, 504000),
#     'Olmzor': (15500, 52045.55, 330000),
#     'Sergeli': (13500, 43673.18, 120000),
#     'Shayhontohur': (21000, 69446.2, 260000),
#     'Uchtepa': (12300, 44558.04, 126000),
#     'Yakkasaroy': (14500, 69535.19, 420000),
#     'Yangihayot': (23000, 37000, 61900),
#     'Yashnobod': (10500, 50671.55, 300000),
#     'Yunusobod': (12500, 62552.72, 425600)
# }

# # Ma'lumotlarni yuklash va unique qiymatlarni olish
# file_path = 'uynarxi.csv'
# data = pd.read_csv(file_path)
# districts = data['district'].unique()

# # Foydalanuvchi kirishlari
# selected_district = st.selectbox("Tumanni tanlang", districts)
# if selected_district in price_ranges:
#     min_price, mean_price, max_price = price_ranges[selected_district]
#     #st.write(f"{selected_district} uchun narxlar diapazoni: Min: {min_price}, O'rtacha: {mean_price}, Max: {max_price}")

# rooms = st.number_input("Xonalar soni", min_value=1, step=1)
# size = st.number_input("Maydoni (m²)", min_value=1.0, step=1.0)
# level = st.number_input("Qavat raqami", min_value=1, step=1)
# max_levels = st.number_input("Umumiy qavatlar soni", min_value=1, step=1)

# # Bashorat qilish tugmasi
# if st.button("Narxni bashorat qilish"):
#     # Foydalanuvchi kiritgan ma'lumotlardan massiv yaratish
#     user_data = {
#         'district': [selected_district],
#         'rooms': [rooms],
#         'size': [size],
#         'level': [level],
#         'max_levels': [max_levels]
#     }

#     # DataFrame yaratish
#     user_df = pd.DataFrame(user_data)

#     # Kategorik ustunni kodlash
#     user_df = pd.get_dummies(user_df, drop_first=True)

#     # Modellashda ishlatilgan ustunlarni tekshirish va to'ldirish
#     model_columns = pd.get_dummies(data.drop(columns=['price']), drop_first=True).columns
#     for col in model_columns:
#         if col not in user_df.columns:
#             user_df[col] = 0

#     # Ustunlarning tartibini moslashtirish
#     user_df = user_df[model_columns]

#     # Bashorat qilish
#     prediction = model.predict(user_df)[0]

#     # Natijani chiqarish
#     st.write(f"Bashorat qilingan uy narxi: {prediction:.2f}")

    

# import streamlit as st
# import pandas as pd
# import numpy as np
# import joblib

# # Modelni yuklash
# model_filename = 'uynarxi.pkl'
# model = joblib.load(model_filename)

# # Sahifa sozlamalari
# st.title("Uy narxini bashorat qilish")
# st.write("Iltimos, uy haqidagi ma'lumotlarni kiriting va narxini bashorat qiling.")

# # Ma'lumotlarni yuklash va unique qiymatlarni olish
# file_path = 'uynarxi.csv'
# data = pd.read_csv(file_path)
# districts = data['district'].unique()

# # Foydalanuvchi kirishlari
# selected_district = st.selectbox("Tumanni tanlang", districts)
# rooms = st.number_input("Xonalar soni", min_value=1, step=1)
# size = st.number_input("Maydoni (m²)", min_value=1.0, step=1.0)
# level = st.number_input("Qavat raqami", min_value=1, step=1)
# max_levels = st.number_input("Umumiy qavatlar soni", min_value=1, step=1)

# # Bashorat qilish tugmasi
# if st.button("Narxni bashorat qilish"):
#     # Foydalanuvchi kiritgan ma'lumotlardan massiv yaratish
#     user_data = {
#         'district': [selected_district],
#         'rooms': [rooms],
#         'size': [size],
#         'level': [level],
#         'max_levels': [max_levels]
#     }

#     # DataFrame yaratish
#     user_df = pd.DataFrame(user_data)

#     # Kategorik ustunni kodlash
#     user_df = pd.get_dummies(user_df, drop_first=True)

#     # Modellashda ishlatilgan ustunlarni tekshirish va to'ldirish
#     model_columns = pd.get_dummies(data.drop(columns=['price']), drop_first=True).columns
#     for col in model_columns:
#         if col not in user_df.columns:
#             user_df[col] = 0

#     # Ustunlarning tartibini moslashtirish
#     user_df = user_df[model_columns]

#     # Bashorat qilish
#     prediction = model.predict(user_df)[0]

#     # Natijani chiqarish
#     st.write(f"Bashorat qilingan uy narxi: {prediction:.2f}")



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


