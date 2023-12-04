-- DROP TABLE IF EXISTS 
-- student,
-- address,
-- parent,
-- student_subject,
-- subject
-- ;
CREATE TABLE IF NOT EXISTS address (
    id SERIAL PRIMARY KEY,
    city VARCHAR(255) NOT NULL,
    pobox VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS subject (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    code VARCHAR (255) NOT NULL
);
CREATE TABLE IF NOT EXISTS parent (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS student (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    parent_id INTEGER REFERENCES parent(id),
    address_id INTEGER NOT NULL UNIQUE REFERENCES address(id),
    subject_id INTEGER REFERENCES subject(id)
);
CREATE TABLE IF NOT EXISTS student_subject (
    id SERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL REFERENCES student(id),
    subject_id INTEGER NOT NULL REFERENCES subject(id),
    UNIQUE(student_id, subject_id)
);
INSERT INTO parent (id, name)
VALUES (1, 'Bett'),
    (2, 'west'),
    (3, 'allain');
INSERT INTO address (id, city, pobox)
VALUES (1, 'Delhi', '2145'),
    (2, 'Doha', '2347'),
    (3, 'Berlin', '5678');
INSERT INTO student (id, name, parent_id, address_id)
VALUES (1, 'Mich', 1, 1);
-- SELECT * FROM student;
-- This commented line would result in an error because it's not properly placed.
-- Retrieve student information with parent's name, address details, and enrolled subjects
SELECT s.*,
    p.name AS parent_name,
    a.*,
    sub.name AS subject_name,
    sub.code AS subject_code
FROM student s
    JOIN parent p ON s.parent_id = p.id
    JOIN address a ON s.address_id = a.id
    LEFT JOIN student_subject ss ON s.id = ss.student_id
    LEFT JOIN subject sub ON ss.subject_id = sub.id;