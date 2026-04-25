# Write your MySQL query statement below
SELECT r.contest_id, ROUND((COUNT(r.contest_id)/(SELECT COUNT(DISTINCT user_id) as user FROM Users)*100),2) as percentage 
FROM Register as r 
LEFT JOIN
users as u
ON r.user_id = u.user_id 
GROUP BY r.contest_id
ORDER BY percentage desc, contest_id asc