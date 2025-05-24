Asteroid Tehlike Analizi ve Kümeleme Projesi
Proje Hakkında
Bu proje, NASA tarafından sağlanan asteroid verilerini kullanarak, asteroidlerin tehlikeli olup olmadığını tahmin etmeyi ve farklı özelliklerine göre gruplandırmayı amaçlamaktadır. Veri biliminde hem gözetimli hem de gözetimsiz öğrenme algoritmaları kullanılarak, asteroidlerin özelliklerinin analiz edilmesi ve sınıflandırılması gerçekleştirilmiştir.

Kullanılan Algoritmalar ve Nedenleri
Gözetimsiz Öğrenme: KMeans Kümeleme
Amaç: Veri setindeki asteroidleri benzer özelliklere sahip gruplara ayırmak.

Neden kullanıldı? Verideki asteroidlerin çap, hız, Dünya'ya yaklaşma mesafesi gibi özelliklerine göre doğal kümeler oluşturmak istedik. Bu, verinin yapısını anlamamıza yardımcı olur ve farklı asteroid türlerini ayırt etmemizi sağlar.

Nasıl uygulandı? est_diameter_min ve est_diameter_max gibi çap bilgileri kullanılarak 3 küme oluşturuldu. Böylece asteroidler çaplarına göre gruplandı.

Gözetimli Öğrenme: Random Forest Sınıflandırması
Amaç: Asteroidlerin tehlikeli (hazardous) olup olmadığını tahmin etmek.

Neden kullanıldı? Tehlike durumu etiketli bir veri olduğundan, bu etiketle model eğitmek için gözetimli öğrenme uygundu. Random Forest, güçlü ve yoruma açık bir sınıflandırma algoritmasıdır, çeşitli özelliklerin (çap, hız, mesafe vb.) tehlike üzerindeki etkisini yakalayabilir.

Nasıl uygulandı? Veri ön işleme ile özellikler hazırlandı ve model eğitildi. Modelin doğruluğu ve performansı, sınıflandırma raporları ile değerlendirildi.

İzlenen Yol ve Adımlar
Veri İncelemesi ve Temizleme: Verideki önemli sütunlar seçildi, eksik veya anlamsız veriler temizlendi.

Kümeleme (KMeans): Asteroidlerin doğal gruplarını görmek için çap değerleri kullanılarak kümeler oluşturuldu.

Özellik Mühendisliği: Model için anlamlı değişkenler seçildi, gerektiğinde yeni özellikler türetildi.

Sınıflandırma (Random Forest): Tehlike etiketini tahmin etmek için model eğitildi ve test edildi.

Değerlendirme: Model performansı accuracy, precision, recall gibi metriklerle ölçüldü.

Görselleştirme: Kümeleme sonuçları grafiklerle, sınıflandırma performansı ise rapor formatında sunuldu.

Sonuç ve Yorumlar
KMeans ile asteroidler çaplarına göre üç ana kümeye ayrıldı. Bu kümeleme, veri yapısını anlamak ve gruplar arasındaki farkları incelemek için faydalı oldu.

Random Forest sınıflandırması, asteroidlerin tehlikeli olup olmadığını tahmin etmede başarılı sonuçlar verdi.

Proje, uzay tehlikelerinin erken tespiti ve sınıflandırılması için veri bilimi yöntemlerinin etkinliğini göstermektedir.

