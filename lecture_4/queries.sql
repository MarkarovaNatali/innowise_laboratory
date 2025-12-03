-- 1. Create table 'students'
create TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,   -- Student's ID
    full_name TEXT NOT NULL,                -- Student's full name
    birth_year INTEGER                      -- Student's birth year
);

-- Create table 'grades'
create TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,   -- Unique rating identifier
    student_id INTEGER NOT NULL,            -- Link to student's ID
    subject TEXT NOT NULL,                  -- Name of subject
    grade REAL,                             -- Grade
    FOREIGN KEY (student_id) REFERENCES students(id)
);

-- 2. Insert sample data
-- Insert students
insert into students (full_name, birth_year)
values ('Alice Johnson', 2005),
       ('Brian Smith', 2004),
       ('Carla Reyes', 2006),
       ('Daniel Kim', 2005),
       ('Eva Thompson', 2003),
       ('Felix Nguyen', 2007),
       ('Grace Patel', 2005),
       ('Henry Lopez', 2004),
       ('Isabella Martinez', 2006);

-- Insert grades
insert into grades (student_id, subject, grade)
values (1, 'Math', 88),
        (1, 'English', 92),
        (1, 'Science', 85),
        (2, 'Math', 75),
        (2, 'History', 83),
        (2, 'English', 79),
        (3, 'Science', 95),
        (3, 'Math', 91),
        (3, 'Art', 89),
        (4, 'Math', 84),
        (4, 'Science', 88),
        (4, 'Physical Education', 93),
        (5, 'English', 90),
        (5, 'History', 85),
        (5, 'Math', 88),
        (6, 'Science', 72),
        (6, 'Math', 78),
        (6, 'English', 81),
        (7, 'Art', 94),
        (7, 'Science', 87),
        (7, 'Math', 90),
        (8, 'History', 77),
        (8, 'Math', 83),
        (8, 'Science', 80),
        (9, 'English', 96),
        (9, 'Math', 89),
        (9, 'Art', 92);

-- Example queries
-- 3. Find all grades for a specific student (Alice Johnson)
SELECT g.grade
FROM grades AS g
JOIN students AS s
ON g.student_id = s.id
WHERE s.full_name = 'Alice Johnson';

-- 4. Calculate the average grades per student
SELECT s.full_name, AVG(g.grade) AS average_grade
FROM students AS s
JOIN grades AS g ON s.id = g.student_id
GROUP BY s.full_name;

-- 5. List all students born afrte 2004
SELECT full_name, birth_year
FROM students
WHERE birth_year > 2004;

-- 6. Create a query that lists all subjects and their average grades
SELECT subject, AVG(grade) AS average_grade
FROM grades
GROUP BY subject;

-- 7. Find the top-3 students with the highest average grates
SELECT s.full_name, AVG(g.grade) AS average_grade
FROM students AS s
JOIN grades AS g ON s.id = g.student_id
GROUP BY s.full_name
ORDER BY average_grade DESC
LIMIT 3;

-- 8. Show all students who have scored below 80 in any subject
SELECT DISTINCT s.full_name
FROM students AS s
JOIN grades AS g ON s.id = g.student_id
WHERE g.grade < 80;