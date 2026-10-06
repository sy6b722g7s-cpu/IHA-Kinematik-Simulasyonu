# İHA Kinematik Yörünge Simülasyonu ve Telemetri Veri Tabanı

Bu proje, bir insansız hava aracının (İHA) üç boyutlu sarmal yükseliş yörüngesini parametrik denklemlerle üretir, konum verisini SQLite veri tabanına aktarır ve SQL sorgularıyla analiz eder.

> **Not:** Proje başlangıçta yapay zeka desteğiyle oluşturuldu. SQL katmanını (tablo şeması, veri yükleme, sorgular) ve sonuçların doğrulamasını kendim kurup çalıştırdım. Yapay zeka destekli geliştirme sürecinde her adımı anlayarak ilerlemeye çalıştım.

## Ne yapıyor?

1. `simulasyon.py` 0-100 saniye arasını 500 noktaya böler (saniyede 5 nokta), yörüngeyi hesaplar, 3 boyutlu grafiğini çizer ve `iha_telemetri.csv` dosyasını üretir.
2. `schema.sql` telemetri tablosunu tanımlar.
3. `yukle_veritabani.py` CSV'yi okuyup `iha_telemetri.db` (SQLite) içindeki `telemetri` tablosuna yazar.
4. `sorgular.sql` tablo üzerinde çalıştırılan analiz sorgularını içerir.

## Matematiksel model

Yörünge parametrik denklemlerle tanımlanmıştır (t: saniye):

- `x(t) = 10 · cos(t/5) · (t/10)`
- `y(t) = 10 · sin(t/5) · (t/10)`
- `z(t) = 50 + 2t`

Bu, yatay düzlemde Arşimet sarmalıdır (yarıçap `r = t`, açısal hız 0,2 rad/s). İrtifa ise sabit 2 m/s ile artar.

**Önemli bulgu:** Kodda `hiz = 10` değişkeni vardır, ancak bu gerçek hız değil, sarmalın büyüklüğünü belirleyen bir ölçek katsayısıdır. Gerçek hız türevden hesaplanabilir. Yatay hız `√(1 + (t/5)²)`, toplam hız ise `√(5 + (t/5)²)` olur, yani İHA'nın hızı sabit değil, zamanla artar. Bu, SQL ile ardışık noktalardan hesaplanan hızla doğrulanmıştır (ilk adımda yaklaşık 2,2 m/s, son adımda yaklaşık 20,1 m/s).

## Veri tabanı

Tablo: `telemetri(id, zaman_sn, x_konum, y_konum, irtifa_m)`

`sorgular.sql` içindeki sorgular:

1. İrtifası 200 m'yi aşan kayıtlar (ilk kayıt yaklaşık 75,15. saniyede, denklemden `50 + 2t = 200 → t = 75` ile uyumlu).
2. İrtifa için özet istatistik (`COUNT`, `MIN`, `MAX`, `AVG`).
3. 50 m'lik irtifa dilimlerine göre gruplama (`GROUP BY`).
4. Ardışık noktalardan uçuş hızı hesabı (`LAG` pencere fonksiyonu ile).

## Çalıştırma

```
pip install numpy pandas matplotlib
python simulasyon.py
python yukle_veritabani.py
```

Ardından `iha_telemetri.db` dosyası herhangi bir SQL aracında (ör. DataGrip) açılıp `sorgular.sql` içindeki sorgular çalıştırılabilir.

## Sınırlılıklar ve sonraki adımlar

- Model kinematiktir: yörünge hazır denklemlerle verilir, kuvvet/ivme tabanlı dinamik çözüm yoktur.
- Sonraki adım: hızdan sayısal integrasyonla (Euler) konumu yeniden üretip analitik çözümle hata karşılaştırması yapmak.
- Sonraki adım: ivme hesabı ve grafikleri.
