import sqlite3
import pandas as pd

veri = pd.read_csv('iha_telemetri.csv')
veri.columns = ['zaman_sn', 'x_konum', 'y_konum', 'irtifa_m']

baglanti = sqlite3.connect('iha_telemetri.db')

with open('schema.sql', 'r', encoding='utf-8') as f:
    baglanti.executescript(f.read())

veri.to_sql('telemetri', baglanti, if_exists='append', index=False)
baglanti.commit()

sonuc = baglanti.execute('SELECT COUNT(*) FROM telemetri').fetchone()
print('Tablodaki satır sayısı:', sonuc[0])

baglanti.close()