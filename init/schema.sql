-- Hubs (centros de distribuição)
CREATE TABLE hubs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    city TEXT NOT NULL
);

-- Riders (entregadores)
CREATE TABLE riders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    hub_id INTEGER,
    FOREIGN KEY (hub_id) REFERENCES hubs(id)
);

-- Orders (pedidos)
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hub_id INTEGER,
    rider_id INTEGER,
    created_at TEXT NOT NULL,
    picked_up_at TEXT,
    delivered_at TEXT,
    status TEXT,
    FOREIGN KEY (hub_id) REFERENCES hubs(id),
    FOREIGN KEY (rider_id) REFERENCES riders(id)
);

CREATE TABLE riders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    hub_id INTEGER,
    FOREIGN KEY (hub_id) REFERENCES hubs(id)
);
