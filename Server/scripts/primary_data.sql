INSERT INTO clients(id, name, full_name, email, login, password)
VALUES (1, 'Vladimir', 'Ivanov', 'vova25072000@bk.ru', 'VIV', 'TsPtsNH2yrpg');

INSERT INTO departments(id, department_name, description)
VALUES (1, 'Administration', 'Employees have the highest degree of database management');

INSERT INTO manufacturers(id, name, contact_information)
VALUES (1, 'OZON_FRESH', '+79958003535');

INSERT INTO categories(id, name, description)
VALUES (1, 'CPU', 'This category is intended for all processors stored in the store''s database');

INSERT INTO staff(id, name, full_name, department_id, date_of_employment, contact_information, position)
VALUES (1, 'Egor', 'Elagin', 1, '2012-09-09 12:12:45.434',
        '32446632', 'ADM');

INSERT INTO orders(id, client_id, date, status, address_delivery, method_payment)
VALUES (1, 1,'2023-12-09 12:23:45.054', 'No', 'Gagarin_10',
        'Bank_card');

INSERT INTO products(id, product_name, description, price, quantity_in_stock,
                     manufacturer_id, category_id, model, specifications)
VALUES (1, 'AMD Ryzen 5 5600X', 'CPU is a good', 3000, 1,
        1, 1, 'AMD', '--');