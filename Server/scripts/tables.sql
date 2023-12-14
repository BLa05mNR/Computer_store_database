CREATE TABLE clients(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NULL,
    login VARCHAR(100) NOT NULL,
    password VARCHAR(25) NOT NULL
);

CREATE TABLE departments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    department_name VARCHAR(100) NOT NULL,
    description VARCHAR(500) NOT NULL
);

CREATE TABLE manufacturers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    contact_information VARCHAR(100) NOT NULL
);

CREATE TABLE categories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(255) NOT NULL
);

CREATE TABLE staff(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    department_id INTEGER,
    date_of_employment VARCHAR(50) NOT NULL,
    contact_information VARCHAR(100) NULL,
    position VARCHAR(100) NULL,
    FOREIGN KEY (department_id)
        REFERENCES departments(id)
            ON DELETE NO ACTION ON UPDATE NO ACTION
);

CREATE TABLE orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER,
    date VARCHAR(50) NOT NULL,
    status VARCHAR(100) NOT NULL,
    address_delivery VARCHAR(100) NOT NULL,
    method_payment VARCHAR(100) NOT NULL,
    FOREIGN KEY(client_id)
        REFERENCES clients(id)
            ON DELETE NO ACTION ON UPDATE NO ACTION
);

CREATE TABLE products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name VARCHAR(100) NOT NULL,
    description VARCHAR(255) NOT NULL,
    price INTEGER NOT NULL,
    quantity_in_stock INTEGER NOT NULL,
    manufacturer_id INTEGER,
    category_id INTEGER,
    model VARCHAR(75) NOT NULL,
    specifications VARCHAR(100) NULL,
    FOREIGN KEY (manufacturer_id)
        REFERENCES manufacturers(id)
            ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY (category_id)
        REFERENCES clients(id)
            ON DELETE NO ACTION ON UPDATE NO ACTION
);