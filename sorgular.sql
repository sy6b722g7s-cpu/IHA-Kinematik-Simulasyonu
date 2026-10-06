-- 1. Irtifasi 200 metreyi asan kayitlar
SELECT * FROM telemetri
WHERE irtifa_m > 200
ORDER BY zaman_sn;

-- 2. Irtifa icin ozet istatistik
SELECT COUNT(*) AS kayit_sayisi,
       MIN(irtifa_m) AS en_dusuk_irtifa,
       MAX(irtifa_m) AS en_yuksek_irtifa,
       AVG(irtifa_m) AS ortalama_irtifa
FROM telemetri;

-- 3. 50 metrelik irtifa dilimlerine gore gruplama
SELECT CAST(irtifa_m / 50 AS INTEGER) * 50 AS irtifa_dilimi,
       COUNT(*) AS kayit_sayisi,
       MIN(zaman_sn) AS baslangic_sn,
       MAX(zaman_sn) AS bitis_sn
FROM telemetri
GROUP BY irtifa_dilimi
ORDER BY irtifa_dilimi;

-- 4. Ardisik noktalardan ucus hizinin hesaplanmasi (m/s)
WITH adimlar AS (
    SELECT zaman_sn,
           x_konum - LAG(x_konum) OVER (ORDER BY zaman_sn) AS dx,
           y_konum - LAG(y_konum) OVER (ORDER BY zaman_sn) AS dy,
           irtifa_m - LAG(irtifa_m) OVER (ORDER BY zaman_sn) AS dz,
           zaman_sn - LAG(zaman_sn) OVER (ORDER BY zaman_sn) AS dt
    FROM telemetri
)
SELECT zaman_sn,
       SQRT(dx*dx + dy*dy + dz*dz) / dt AS hiz_m_s
FROM adimlar
WHERE dt IS NOT NULL
ORDER BY zaman_sn;