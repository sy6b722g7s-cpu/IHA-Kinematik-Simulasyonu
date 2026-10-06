
DROP TABLE IF EXISTS telemetri;

CREATE TABLE telemetri (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    zaman_sn REAL NOT NULL,
    x_konum REAL NOT NULL,
    y_konum REAL NOT NULL,
    irtifa_m REAL NOT NULL
);
