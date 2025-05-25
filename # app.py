# app.py
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import IsolationForest
from sklearn.cluster import KMeans
import lightgbm as lgb
from sklearn.metrics import classification_report, confusion_matrix
import os
import warnings

warnings.filterwarnings("ignore")

# Sayfa ayarları
st.set_page_config(page_title="NASA NEO ML", layout="wide")

# Başlık
st.title("🚀 Akbank Global AI Hub - NASA NEO ML Analiz Arayüzü")
st.markdown("""
Bu uygulama [bu notebook'a](https://github.com/hanimbasturkk/akbank-nasa-neo-ml/blob/main/akbankglobalaihubsupervised.ipynb) dayanarak Streamlit ile geliştirilmiştir.  
Veri kümesi: [NASA NEO Kaggle](https://www.kaggle.com/competitions/akbank-ai-global-ai-hub-nasa-neo/overview)
""")

# Veri Yükleme
@st.cache_data
def load_data():
    df = pd.read_csv("/mnt/data/akbankglobalaihubsupervised.ipynb")  # Özgün veri değil, gerçek CSV lazımsa buraya yüklenmeli
    return df

# NOT: Aşağıdaki CSV dosyası sizin tarafınızdan aynı dizine "neo.csv" adıyla yüklenmelidir.
data_path = "/mnt/data/neo.csv"
if os.path.exists(data_path):
    df = pd.read_csv(data_path)
else:
    st.error("Lütfen 'neo.csv' dosyasını yükleyin!")
    st.stop()

# Seçim menüsü
section = st.sidebar.radio("🧭 Hangi bölümü incelemek istersiniz?", (
    "Veri Önizleme",
    "Eksik Veriler & Sınıf Dengesi",
    "Korelasyon Analizi",
    "Kümeleme & Anomali Tespiti",
    "Model Eğitimi ve Tahmin",
))

# --- Veri Önizleme
if section == "Veri Önizleme":
    st.subheader("📄 Veri Önizleme")
    st.write(df.head())
    st.write("🔢 Veri Şekli:", df.shape)
    st.write("🧬 Sütunlar:", df.columns.tolist())

# --- Eksik Veriler ve Sınıf Dengesi
elif section == "Eksik Veriler & Sınıf Dengesi":
    st.subheader("🔍 Eksik Veriler Analizi")
    missing = df.isnull().sum()
    st.write(missing[missing > 0])

    st.subheader("⚖️ Sınıf Dengesi")
    if 'Hazardous' in df.columns:
        sns.countplot(data=df, x='Hazardous')
        st.pyplot(plt.gcf())
        plt.clf()

# --- Korelasyon Analizi
elif section == "Korelasyon Analizi":
    st.subheader("📊 Korelasyon Matrisi")
    corr = df.corr()
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    st.pyplot(fig)

# --- Kümeleme & Anomali Tespiti
elif section == "Kümeleme & Anomali Tespiti":
    st.subheader("🔵 KMeans Kümeleme")
    numeric_cols = df.select_dtypes(include=np.number).dropna(axis=1).columns.tolist()
    x_cols = st.multiselect("Kümeleme için değişkenleri seçin", options=numeric_cols, default=numeric_cols[:2])
    if len(x_cols) >= 2:
        kmeans = KMeans(n_clusters=3)
        clusters = kmeans.fit_predict(df[x_cols])
        df["cluster"] = clusters
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x=x_cols[0], y=x_cols[1], hue="cluster", palette="tab10", ax=ax)
        st.pyplot(fig)

    st.subheader("🚨 Isolation Forest ile Anomali Tespiti")
    iso = IsolationForest(contamination=0.05)
    preds = iso.fit_predict(df[numeric_cols])
    df["anomaly"] = preds
    st.write(df["anomaly"].value_counts())

# --- Model Eğitimi ve Tahmin
elif section == "Model Eğitimi ve Tahmin":
    st.subheader("🎓 Model Eğitimi (LightGBM)")

    if 'Hazardous' not in df.columns:
        st.error("'Hazardous' adlı hedef değişken bulunamadı.")
        st.stop()

    target = "Hazardous"
    features = df.select_dtypes(include=np.number).drop(columns=[target]).columns.tolist()

    test_size = st.slider("Test veri oranı", 0.1, 0.5, 0.2)
    random_state = st.number_input("Rastgele tohum", 0, 10000, 42)

    X_train, X_test, y_train, y_test = train_test_split(df[features], df[target], test_size=test_size, random_state=random_state)

    model = lgb.LGBMClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    st.text("Classification Report:")
    st.text(classification_report(y_test, y_pred))

    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax)
    ax.set_title("Confusion Matrix")
    st.pyplot(fig)
