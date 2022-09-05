/*
Retail Store Employees Data Exploration 
Skills used: Query Basics, Aggregate Functions, Subqueries, Pipes, Transposing Data
*/

-- Filtering on multiple conditions
SELECT *
FROM employees
WHERE salary < 40000
AND (department = 'Clothing'
OR department = 'Pharmacy');

-- Return the first_name and email of females that work in the tools department that earn more than 40,000 and less than 100,000, as well as males that work in the Sports dept.
SELECT first_name, email
FROM employees
WHERE gender = 'F'
AND department = 'Tools'
AND salary BETWEEN 40000 AND 100000
OR (gender = 'M' AND department = 'Sports');

--The salary of an employee must not be less than age  if their hire date is either between 2003-01-01 and 2010-01-01 or their region_id is 2. Your query should also return employes that started after 2014-11-08 but in that case they must have a salary that is at least 50000.
SELECT *
FROM employees
WHERE salary <= 30000 
AND (hire_date BETWEEN '2003-01-01' AND '2010-01-01' OR region_id = 2)
OR (hire_date >= '2014-11-08' AND salary >= 50000);

/*
Conditional expressions and Concatenation
*/

--Ouputs the following result: "Cy Mence works in the Automotive department under the divsion" for all employees
SELECT first_name || ' ' || last_name || ' works in the ' || department || ' department under the ' || (SELECT division FROM departments WHERE department ='Automotive') || ' divison.'
FROM employees

/*Grouping and Subqueries
*/

--A query that groups the unique domain names from emails and the number of employees using those domain names
--and orfder them by the most popular domain names
SELECT SUBSTRING(email,POSITION('@' IN email) + 1) domain_name, count(*) employees
FROM employees
WHERE email IS NOT NULL
GROUP BY domain_name
ORDER BY count(*) DESC

--Returns all the employees that work in either Asia or Canada and make over 130000.
SELECT *
FROM employees
WHERE salary >= 130000 AND region_id
	IN (SELECT region_id FROM regions WHERE country = 'Asia' OR country = 'Canada')
	
--Show the first_name and the department they are in and how much less they make than the highest paid employee + they must be working in the US or Canada.
SELECT first_name, department, salary, (SELECT MAX(salary) FROM employees), ((SELECT MAX(salary) FROM employees) - salary) as difference, region_id
FROM employees
WHERE region_id IN (SELECT region_id FROM regions WHERE country IN ('United States','Canada'))
ORDER BY difference

--Computes average of all employees salary but exclude the min and max value (Eliminating Outliers)

SELECT ROUND(AVG(salary))
FROM employees
WHERE salary NOT IN(
(SELECT MIN(salary) FROM employees),
(SELECT MAX(salary)FROM employees)
)

--Transpose the following table so that the column headers are the departments
SELECT department, count(*)
FROM employees
WHERE department IN ('Sports', 'Tools', 'Clothing', 'Computers')
GROUP BY department

SELECT SUM(CASE WHEN department = 'Sports' THEN 1 ELSE 0 END) as sports_employees,
	SUM(CASE WHEN department = 'Tools' THEN 1 ELSE 0 END) as hardware_employees,
	SUM(CASE WHEN department = 'Clothing' THEN 1 ELSE 0 END) as living_employees,
	SUM(CASE WHEN department = 'Computers' THEN 1 ELSE 0 END) as tech_employees
FROM employees

-- Return the total counts of employees according to their salary and assign a position.
SELECT SUM(CASE WHEN salary < 100000 THEN 1 ELSE 0 END) as under_paid,
	SUM(CASE WHEN salary > 100000 AND salary < 160000 THEN 1 ELSE 0 END) as paid_well,
	SUM(CASE WHEN salary > 160000 THEN 1 ELSE 0 END) as executive
FROM employees
