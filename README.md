# 🚀 Asteroid Tehlike Analizi ve Kümeleme Projesi

<img src="Ekran görüntüsü 2025-05-25 2334" 
---

## 📝 Proje Hakkında
NASA'nın sağladığı **asteroid verileri** kullanılarak, bu gök cisimlerinin tehlike durumlarını anlamak ve gruplamak amacıyla geliştirilen bir makine öğrenmesi projesidir.  
Projede hem **gözetimsiz** hem de **gözetimli öğrenme** algoritmaları kullanılmıştır.

---

## 🔍 Kullanılan Algoritmalar & Amaçları

### 1. Gözetimsiz Öğrenme: **KMeans Kümeleme**

- **Amaç:**  
Asteroidleri benzer fiziksel özelliklerine göre gruplandırmak.  
- **Neden KMeans?**  
Verideki doğal kümeleri ortaya çıkarmak ve asteroidlerin çap gibi özelliklerine göre sınıflandırmak için hızlı ve etkili bir yöntem.  
- **Nasıl?**  
`est_diameter_min` ve `est_diameter_max` özellikleri kullanılarak **3 küme** oluşturulmuş ve asteroidler bu kümelere atanmıştır.

---

### 2. Gözetimli Öğrenme: **Random Forest Sınıflandırması**

- **Amaç:**  
Asteroidlerin **tehlikeli (hazardous)** olup olmadığını tahmin etmek.  
- **Neden Random Forest?**  
  - Çok sayıda özelliğin etkisini analiz etmekte başarılıdır.  
  - Yüksek doğruluk ve kararlılık sağlar.  
  - Yorumu görece kolaydır.  
- **Nasıl?**  
Veri temizlendikten sonra model eğitilmiş ve performansı doğruluk, kesinlik, geri çağırma gibi metriklerle değerlendirilmiştir.

---

## 🛤️ İzlenen Yol

1. **Veri Hazırlama:**  
   - Eksik ve tutarsız veriler temizlendi.  
   - Kullanılacak özellikler seçildi.  

2. **Kümeleme Uygulaması:**  
   - Asteroidler çaplarına göre kümelere ayrıldı.  
   - Sonuçlar grafiklerle görselleştirildi.  

3. **Sınıflandırma Modeli:**  
   - `hazardous` etiketi hedef değişken olarak seçildi.  
   - Random Forest modeli eğitildi ve test edildi.  

4. **Sonuçların Analizi:**  
   - Küme yapıları ve sınıflandırma başarısı yorumlandı.

---

## 📊 Sonuçlar & Yorumlar

- KMeans algoritması asteroidleri çap bazlı 3 anlamlı kümeye ayırdı.  
- Random Forest modeli, asteroidlerin tehlike durumlarını tahmin etmede yüksek başarı sağladı.  
- Veri bilimi teknikleri, uzaydaki potansiyel tehlikelerin erken tespitinde güçlü araçlardır.


---

> **Not:** Bu proje, veri bilimi teknikleriyle uzaydaki tehlikelerin tespiti konusunda somut adımlar atmayı amaçlamaktadır.

---
kaggle linkleri:

https://www.kaggle.com/code/hanmbatrk/akbankglobalaihubsupervised
https://www.kaggle.com/code/hanmbatrk/akbankglobalaihubunsupervised



