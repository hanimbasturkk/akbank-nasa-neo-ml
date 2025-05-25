import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

# Veriyi oku
data_path = os.path.join("..", "data", "neo.csv")
df = pd.read_csv(data_path)

# Özellikler ve hedef sütunu seç
X = df[["est_diameter_min", "est_diameter_max", "relative_velocity", "miss_distance", "absolute_magnitude"]]
y = df["hazardous"]

# Modeli eğit
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Modeli kaydet
with open("models/neo_model.pkl", "rb") as f:
    pickle.dump(clf, f)

print("Model başarıyla eğitildi ve kaydedildi.")
