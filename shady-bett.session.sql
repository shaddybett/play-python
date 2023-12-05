CREATE TABLE locations(
    id SERIAL PRIMARY KEY,
    country VARCHAR(250)
);
CREATE TABLE cub(
    id SERIAL PRIMARY KEY,
    name VARCHAR(250) NOT NULL
);
CREATE TABLE lion(
    id SERIAL PRIMARY KEY,
    name VARCHAR(250) NOT NULL,
    cub_id INTEGER REFERENCES cub(id)
);
CREATE TABLE animals(
    id SERIAL PRIMARY KEY,
    name VARCHAR(250) NOT NULL,
    top_animal INTEGER REFERENCES lion (id)
);
CREATE TABLE park(
    id SERIAL PRIMARY KEY,
    name VARCHAR(250) NOT NULL,
    locations_id INTEGER REFERENCES locations (id),
    animals_id INTEGER REFERENCES animals (id)
);
INSERT INTO locations(id, country)
VALUES (1, 'Tanzania'),
    (2, 'Kenya');
INSERT INTO cub(id, name, lion_id)
VALUES (1, 'Shibli', 1),
    (2, 'Bob', NULL);
INSERT INTO lion(id, name, cub_id)
VALUES (1, 'Simba', 1),
    (2, 'Mufasa', NULL);
INSERT INTO animals(id, name, top_animal)
VALUES (1, 'Lion', 1),
    (2, 'Skunk', NULL);
INSERT INTO park(id, name, locations_id, animals_id)
VALUES (1, 'Kruger', 1, 1),
    (2, 'Tsavo', 2, 2);
-- JOIN Statements
SELECT *
FROM locations
    INNER JOIN park ON park.locations_id = locations.id;
SELECT *
FROM animals
    INNER JOIN lion ON lion.id = animals.top_animal;
SELECT *
FROM lion
    INNER JOIN cub ON lion.id = cub.lion_id;
SELECT *
FROM cub
    INNER JOIN lion ON cub.lion_id = lion.id;