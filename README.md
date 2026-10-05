# İHA Kinematik Yörünge Simülasyonu ve Telemetri Veri Tabanı Modeli

## 📌 Projenin Amacı
Bu proje, bir İnsansız Hava Aracının (İHA) 3 boyutlu uzaydaki uçuş dinamiklerini **matematiksel olarak modellemek**, nümerik simülasyonunu gerçekleştirmek ve uçuş esnasında üretilen anlık telemetri verilerini ilişkisel veri tabanlarına (SQL) aktarılabilecek yapısal bir formata dönüştürmek amacıyla geliştirilmiştir.

## 🛠️ Kullanılan Teknolojiler
* **Python:** Nümerik hesaplamalar ve ana simülasyon döngüsü.
* **NumPy:** Vektörel işlemler ve zaman serisi (zaman dizisi) üretimi.
* **Matplotlib (mpl_toolkits):** 3D yörünge görselleştirmesi.
* **Pandas:** Simülasyon verilerinin tablo (Dataframe) formatına getirilip CSV olarak dışa aktarılması.

## ⚙️ Matematiksel Modelleme (Kinematik Yaklaşım)
Simülasyonda İHA'nın giderek genişleyen ve yükselen bir "sarmal (spiral)" rota izlemesi hedeflenmiştir. Bu yörünge, parametrik denklemler kullanılarak modellenmiştir:

* **X ve Y Eksenleri (Düzlem Hareketi):** Zaman (t) değişkenine bağlı olarak genişleyen bir çember çizmek için trigonometrik fonksiyonlar kullanılmıştır. Zaman ilerledikçe genlik arttığı için hareket dışa doğru açılan bir sarmala dönüşür.
  * `X = Hız * Cos(t/5) * (t/10)`
  * `Y = Hız * Sin(t/5) * (t/10)`
* **Z Ekseni (İrtifa Hareketi):** İrtifa artışı zamana bağlı lineer bir fonksiyon olarak tanımlanmıştır. Araç sabit bir taban yüksekliğinden başlayarak düzenli irtifa kazanır.
  * `Z = 50 + (2 * t)`

##  Veri Yönetimi ve SQL Entegrasyon Vizyonu
Simülasyon çalıştığında saniyede binlerce "anlık konum ve zaman" verisi üretilmektedir. Bu çalışmada üretilen ham veri seti (Zaman, X, Y, İrtifa), `iha_telemetri.csv` olarak dışa aktarılmaktadır. 

Bu veri setinin yapısal tasarımı, doğrudan PostgreSQL veya Microsoft SQL Server gibi ilişkisel veri tabanlarına aktarılmaya uygun şemada hazırlanmıştır. Gerçek dünya senaryosunda bu veriler üzerinden SQL ile;
* Belirli irtifa aralıklarındaki davranış analizleri,
* Konum değişim hızına (türev) bağlı ivme hesaplamaları gibi sorgulamalar yapılabilir.

##  Kurulum ve Çalıştırma
Projeyi kendi ortamınızda çalıştırmak için:
1. Gerekli kütüphaneleri yükleyin: `pip install numpy pandas matplotlib`
2. Ana dosyayı çalıştırın: `python simulasyon.py`
3. 3 boyutlu grafik ekranda açılacak ve telemetri dosyası dizine kaydedilecektir.
