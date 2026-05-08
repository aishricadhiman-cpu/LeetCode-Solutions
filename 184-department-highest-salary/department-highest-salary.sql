# Write your MySQL query statement below
SELECT d.name as Department, e.name as Employee, e.salary
FROM   
(SELECT name,id,departmentId,salary,
MAX(Salary) OVER(PARTITION BY departmentId) as highest_salary
FROM Employee) e
LEFT JOIN Department as d
ON e.departmentId = d.id
WHERE e.salary = e.highest_salary




