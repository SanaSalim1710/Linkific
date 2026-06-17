CREATE DATABASE students_db;

CREATE TYPE gender_type AS ENUM ('Male', 'Female');
CREATE TYPE enrollment_status AS ENUM ('Active', 'Graduated', 'Suspended', 'Withdrawn');

--students table
CREATE TABLE students (
    id              integer PRIMARY KEY GENERATED ALWAYS AS IDENTITY (sequence name "students_id_seq"),
    name            VARCHAR(100) NOT NULL,
    gpa             NUMERIC(3, 2) CHECK (gpa >= 0.0 AND gpa <= 4.0),
    gender          gender_type NOT NULL,
    honours         BOOLEAN,
    email           VARCHAR(320) UNIQUE NOT NULL,
    date_of_birth   DATE NOT NULL,
);

CREATE TABLE classes (
    id SERIAL PRIMARY KEY,
    class_name VARCHAR(100) NOT NULL
);

CREATE TABLE student_classes (
    id SERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL,
    class_id INTEGER NOT NULL,
    final_grade VARCHAR(2),
    FOREIGN KEY (student_id)
        REFERENCES students(id),
    FOREIGN KEY (class_id)
        REFERENCES classes(id)
);

INSERT INTO  classes (class_name) VALUES
    ('Math'),
    ('English'),
    ('Physics'),
    ('Chemistry');

INSERT INTO students (name, gpa, gender, honours, email, date_of_birth) VALUES
    ('Olivia Rodrigo', 4.00, 'Female', TRUE, 'oliviarodrigo@gmail.com',   '2003-02-12'),
    ('Ariana Grande', 3.67,  'Female', TRUE, 'ariana@gmail.com',     '2013-03-15'),
    ('Caleb Tan', 2.14, 'Male', FALSE, 'caleb@gmail.com',   '2021-06-09'),
    ('Corey Smith', 1.80, 'Male', TRUE,   'corey@gmail.com',   '2019-06-12'),
    ('Alyssa Soh', 3.30,  'Female', TRUE,   'alyssa@gmail.com',     '2020-07-16'),
    ('Benedict Cumberbatch', 2.30, 'Male', FALSE,   'ben@gmail.com',   '2018-03-06'),
    ('Perrie Edwards', 2.80, 'Female', FALSE,    'perrie@gmail.com',   '2016-09-16'),
    ('Jade Thirlwall', 3.00, 'Female', TRUE,  'jade@gmail.com',   '2015-10-17'),
    ('Leigh Anne Pinnock', 2.50, 'Female', FALSE, 'leigh@gmail.com',   '2022-05-16'),
    ('Kenny Lee', 3.60, 'Male', TRUE,   'kenny@gmail.com',   '2005-07-20');

INSERT INTO student_classes (student_id, class_id, final_grade)VALUES
(1, 1, 'A'),
(1, 2, 'A+'),
(2, 3, 'D'),
(2, 4, 'A-'),
(3, 2, 'C+'),
(3, 4, 'D+'),
(5, 1, 'A'),
(5, 2, 'A+'),
(5, 4, 'B+'),
(6, 1, 'C'),
(7, 1, 'A'),
(7, 2, 'A+'),
(7, 4, 'B+'),
(8, 2, 'A+'),
(8, 3, 'B'),
(9, 2, 'A+'),
(9, 4, 'F'),
(10, 3, 'B'),
(10, 4, 'B-');

-- view all students
SELECT * FROM students;

-- view only columns name, gpa and honours from students
SELECT name, gpa, honours
FROM students;

-- view name,gpa and gender of female students with gpa >= 3
SELECT name, gpa, gender
FROM students
WHERE gpa >= 3.00 AND gender = 'Female';

-- view name, gpa, email of students sorted by gpa in descending order
SELECT name, gpa, email
FROM students
ORDER BY gpa DESC;

-- view honours (T/F) and new column avg_gpa containing average gpa of hons students and non-hons students
SELECT honours, ROUND(AVG(gpa), 2) AS avg_gpa
FROM students
GROUP BY honours;

-- insert new student
INSERT INTO students (name, gpa, gender, honours, email, date_of_birth)
VALUES ('Scarlet Witch', 2.7, 'Female', FALSE, 'wanda@gmail.com', '2002-06-10');

-- update gpa 
UPDATE students
SET gpa = 3.60
WHERE email = 'leigh@gmail.com';

-- changing back to original value
UPDATE students
SET gpa = 2.5
WHERE email = 'leigh@gmail.com';

-- delete student by id
DELETE FROM students 
WHERE id = 11;

-- order male and female students by gpa in descending order 
-- and gender in ascending order (showed male then female)
SELECT name, gender, gpa
FROM students
ORDER BY gender ASC, gpa DESC;

-- count number of female students
SELECT COUNT(gender) as female_students
FROM students
WHERE gender = 'Female';

-- find highest gpa
SELECT MAX(gpa) as highest_gpa
FROM students;

-- check sum of gpas of all students just to test sum 
SELECT SUM(gpa) as sum_of_gpas
FROM students;

-- view how many hons and non-hons students there are 
-- descending order by count 
-- honours has 6 and non-hons has 4 so hons first then non-hons
SELECT honours, COUNT(*) AS count
FROM students
GROUP BY honours
ORDER BY count DESC;

-- shows students with gpa above average in descending order
SELECT name, gpa
FROM students
WHERE gpa > (SELECT AVG(gpa) FROM students)
ORDER BY gpa DESC;

-- shows which classes students are enrolled in
-- shows students even if they arent enrolled in a class
-- left join example
SELECT
    s.name,
    c.class_name
FROM students s
LEFT JOIN student_classes sc
    ON s.id = sc.student_id
LEFT JOIN classes c
    ON sc.class_id = c.id;

-- shows student name, name of classes enrolled in and final grade in the subject
-- does not show if not enrolled in anything
-- inner join example
SELECT
    s.name,
    c.class_name,
    sc.final_grade
FROM student_classes sc
INNER JOIN students s
    ON sc.student_id = s.id
INNER JOIN classes c
    ON sc.class_id = c.id;

INSERT INTO classes (class_name)
VALUES ('History');

-- shows students(names) belonging to each class
-- shows history (right table) even though no students are enrolled
-- example of right join
SELECT
    s.name,
    c.class_name
FROM student_classes sc
RIGHT JOIN classes c
    ON sc.class_id = c.id
LEFT JOIN students s
    ON sc.student_id = s.id;

