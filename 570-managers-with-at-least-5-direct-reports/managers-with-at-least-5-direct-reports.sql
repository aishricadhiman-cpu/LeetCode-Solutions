# Write your MySQL query statement below
select name from Employee where id in (SELECT managerId
FROM Employee
GROUP BY managerId
HAVING COUNT(managerId) >= 5
)