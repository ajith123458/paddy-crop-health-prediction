\# 📌 Paddy Crop Health Prediction System 🌾



\## 🎯 Objective



To develop a machine learning-based system that predicts \*\*paddy crop health\*\* using satellite-derived vegetation indices and environmental factors, helping in early detection of crop stress and better decision-making.



\---



\## 📊 Data Source / Generation



Dataset was generated using \*\*Google Earth Engine (GEE)\*\* from real satellite and weather data.



\### Features used:



\* 🌱 \*\*NDVI\*\* (Normalized Difference Vegetation Index) – crop health

\* 🌿 \*\*EVI\*\* (Enhanced Vegetation Index) – dense vegetation accuracy

\* 🌊 \*\*NDWI\*\* (Normalized Difference Water Index) – water condition

\* 🌧️ \*\*Rainfall\*\* – water availability

\* 🌡️ \*\*Temperature\*\* – environmental condition



👉 Data collected from:



\* Sentinel-2 satellite imagery

\* ERA5 weather dataset

\* CHIRPS rainfall dataset



\---



\## ⚙️ Approach



\### 1️⃣ Data Collection



\* Extracted satellite images from GEE

\* Calculated NDVI, NDWI, and EVI

\* Integrated weather data (temperature, rainfall)



\---



\### 2️⃣ Data Preprocessing



\* Removed unnecessary features (e.g., humidity)

\* Handled missing values

\* Structured dataset for ML



\---



\### 3️⃣ Label Creation



\* Crop health labeled based on NDVI values:



&#x20; \* 0 → Poor ❌

&#x20; \* 1 → Medium ⚠️

&#x20; \* 2 → Healthy ✅



\---



\### 4️⃣ Exploratory Data Analysis (EDA)



\* Visualized feature relationships using:



&#x20; \* Heatmaps

&#x20; \* Boxplots

\* Identified important features:



&#x20; \* NDVI, EVI, Rainfall



\---



\### 5️⃣ Model Building



Trained multiple machine learning models:



\* 🌳 Random Forest

\* ⚡ XGBoost



👉 Random Forest performed well due to:



\* Better handling of nonlinear data

\* Robust performance



\---



\### 6️⃣ Model Evaluation



Used standard metrics:



\* Accuracy

\* Precision

\* Recall

\* F1-score



👉 Model achieved \*\*good balanced performance\*\*



\---



\### 7️⃣ Prediction System



\* Built a \*\*Flask web application\*\*

\* User inputs:



&#x20; \* NDVI, EVI, NDWI, rainfall, temperature

\* Output:



&#x20; \* Predicted crop health (0 / 1 / 2)



\---



\## 🚧 Challenges Faced



\* ❌ NDVI confusion in mature stage (brown crop)

&#x20; ✔️ Solved using additional indices (EVI, NDWI)



\* ❌ Same values in weather data

&#x20; ✔️ Accepted as coarse-resolution limitation



\* ❌ Imbalanced dataset

&#x20; ✔️ Improved sampling strategy



\---



\## 🚀 Future Improvements



\* Integrate \*\*real-time satellite data\*\*

\* Add \*\*weather API (live data)\*\*

\* Include \*\*crop stage detection\*\*

\* Deploy as \*\*cloud-based application\*\*



\---



\## 🧠 Tech Stack



\* Python

\* Pandas, NumPy

\* Scikit-learn

\* Flask

\* Matplotlib, Seaborn

\* Google Earth Engine (GEE)



\---



\## 📌 Conclusion



This project demonstrates how \*\*remote sensing + machine learning\*\* can be used to predict crop health effectively, supporting smarter agricultural practices.



\---



