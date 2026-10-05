import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. Matematiksel Modelleme: 0'dan 100 saniyeye kadar zaman serisi
zaman = np.linspace(0, 100, 500)

# İHA'nın yörünge ve kinematik denklemleri (Sarmal yükseliş modeli)
hiz = 10
x_koordinat = hiz * np.cos(zaman / 5) * (zaman / 10)
y_koordinat = hiz * np.sin(zaman / 5) * (zaman / 10)
z_irtifa = 50 + 2 * zaman  # Giderek yükselen irtifa

# 2. 3 Boyutlu Görselleştirme (Simülasyon Çıktısı)
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_koordinat, y_koordinat, z_irtifa, label='İHA Uçuş Rotası', color='red', linewidth=2)

ax.set_title('İHA 3D Yörünge Simülasyonu (Nümerik Model)')
ax.set_xlabel('X Ekseni (Doğu-Batı)')
ax.set_ylabel('Y Ekseni (Kuzey-Güney)')
ax.set_zlabel('Z Ekseni (İrtifa - Metre)')
ax.legend()
plt.show()

# 3. Veri Tabanı İçin Telemetri Loglarını Kaydetme
veri = pd.DataFrame({
    'Zaman_sn': zaman,
    'X_Konum': x_koordinat,
    'Y_Konum': y_koordinat,
    'Irtifa_m': z_irtifa
})
veri.to_csv('iha_telemetri.csv', index=False)
print("Simülasyon tamamlandı. Grafik çizildi ve veri 'iha_telemetri.csv' olarak kaydedildi.")