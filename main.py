from fpdf import FPDF
from fpdf.enums import XPos, YPos

class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 12)
        self.cell(0, 10, "SQL Commands Cheat Sheet & Practice Set", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("Helvetica", "B", 11)
        self.set_fill_color(220, 220, 220)
        self.cell(0, 8, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="L", fill=True)
        self.ln(2)

    def chapter_body(self, body):
        self.set_font("Helvetica", "", 10)
        self.multi_cell(0, 6, body)
        self.ln()

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

sections = [
    ("1. DDL Commands", """\
CREATE TABLE Students (id INT, name VARCHAR(50));
ALTER TABLE Students ADD email VARCHAR(100);
DROP TABLE Students;
TRUNCATE TABLE Students;
RENAME TABLE Students TO Learners;"""),

    ("2. DML Commands", """\
INSERT INTO Students (id, name) VALUES (1, 'Rudra');
UPDATE Students SET name='Rohan' WHERE id=1;
DELETE FROM Students WHERE id=1;"""),

    ("3. DQL Commands", """\
SELECT * FROM Students;
SELECT name FROM Students WHERE id = 2;"""),

    ("4. DCL Commands", """\
GRANT SELECT, INSERT ON Students TO 'user1';
REVOKE INSERT ON Students FROM 'user1';"""),

    ("5. TCL Commands", """\
START TRANSACTION;
DELETE FROM Enrollments WHERE student_id = 3;
ROLLBACK;
COMMIT;"""),

    ("6. Clauses & Joins", """\
SELECT * FROM Students WHERE id = 2;
SELECT * FROM Students ORDER BY name ASC;
SELECT COUNT(*), course FROM Students GROUP BY course HAVING COUNT(*) > 2;

-- JOINS
SELECT s.name, c.course_name FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id;"""),

    ("7. Sample DB: CollegeDB (Schema)", """\
CREATE TABLE Students (
  student_id INT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE,
  age INT CHECK(age >= 17)
);

CREATE TABLE Courses (
  course_id INT PRIMARY KEY,
  course_name VARCHAR(100) NOT NULL,
  department VARCHAR(50)
);

CREATE TABLE Enrollments (
  enroll_id INT PRIMARY KEY,
  student_id INT,
  course_id INT,
  enrollment_date DATE,
  FOREIGN KEY (student_id) REFERENCES Students(student_id),
  FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);"""),

    ("8. Sample Data Inserts", """\
INSERT INTO Students VALUES
(1, 'Rudra', 'rudra@example.com', 20),
(2, 'Aditi', 'aditi@example.com', 22),
(3, 'Rohan', 'rohan@example.com', 21);

INSERT INTO Courses VALUES
(101, 'Data Structures', 'CSE'),
(102, 'Operating Systems', 'CSE'),
(103, 'Biochemistry', 'Biotech');

INSERT INTO Enrollments VALUES
(1001, 1, 101, '2025-07-01'),
(1002, 1, 102, '2025-07-02'),
(1003, 2, 103, '2025-07-03'),
(1004, 3, 101, '2025-07-04');"""),

    ("9. Practice Queries", """\
-- Basic
SELECT * FROM Students;
SELECT name FROM Students WHERE age > 20;

-- Joins
SELECT s.name, c.course_name
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id;

-- Group By
SELECT c.course_name, COUNT(e.student_id) AS total_students
FROM Courses c
JOIN Enrollments e ON c.course_id = e.course_id
GROUP BY c.course_name;

-- Subqueries
SELECT name FROM Students
WHERE student_id IN (
  SELECT student_id FROM Enrollments
  WHERE course_id = 101
);

-- Update & Delete
UPDATE Students SET age = 23 WHERE student_id = 1;
DELETE FROM Courses WHERE course_id = 103;""")
]

for title, body in sections:
    pdf.chapter_title(title)
    pdf.chapter_body(body)

# Save to desktop or preferred folder
pdf_path = r"C:\Users\tatai\OneDrive\Desktop\SQL_CheatSheet_Practice_Set.pdf"
pdf.output(pdf_path)
print(f"✅ PDF saved to: {pdf_path}")
