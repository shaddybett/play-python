CREATE TABLE park(
    id SERIAL PRIMARY KEY,
    name VARCHAR(250) NOT NULL,
    location REFERENCES location (id)
    animals REFERENCES animals (id)
);
CREATE TABLE location(
    id SERIAL PRIMARY KEY,
    code INTEGER,
);
CREATE TABLE animals(
    id SERIAL PRIMARY KEY,
    name VARCHAR(250) NOT NULL,
    top_animal REFERENCES lion (id)
);
CREATE TABLE lion(
    id SERIAL PRIMARY KEY,
    name VARCHAR(250) NOT NULL,
    cub REFERENCES cub (id)
);
CREATE TABLE cub(
    id SERIAL PRIMARY KEY,
    name VARCHAR(250) NOT NULL,
    lion REFERENCES lion (id)
)
INSERT INTO park(id,name)
VALUES
(1,'Kruger'),
(2,'Tsavo')

INSERT INTO location(id,name)
VALUES
(1,'Tanzania'),
(2,'Kenya')

INSERT INTO animals(id,name)
VALUES
(1,'Lion'),
(2,'Skunk')

INSERT INTO cub(id,name)
VALUES
(1,'Shibli'),
(2,'bob')



