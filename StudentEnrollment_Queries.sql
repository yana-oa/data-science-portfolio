--Advanced Queries Student Enrollment Data

-- a query that shows the student's name, the courses the student is taking and the professors that teach that course.
SELECT student_name, se.course_no, p.last_name
FROM students s
INNER JOIN student_enrollment se
    ON s.student_no = se.student_no
INNER JOIN teach t
    ON se.course_no = t.course_no
INNER JOIN professors p
    ON t.last_name = p.last_name
ORDER BY student_name;

--Only one professor from each course (removing redundancy)
SELECT student_name, course_no, min(last_name)
FROM (
	SELECT student_name, se.course_no, p.last_name
	FROM students s
	INNER JOIN student_enrollment se
		ON s.student_no = se.student_no
	INNER JOIN teach t
		ON se.course_no = t.course_no
	INNER JOIN professors p
		ON t.last_name = p.last_name
		) a
GROUP BY student_name, course_no
ORDER BY student_name, course_no;

--a query that returns ALL of the students as well as any courses they may or may not be taking.
SELECT s.student_no, student_name, course_no
FROM students s LEFT JOIN student_enrollment se
    ON s.student_no = se.student_no
