SELECT DISTINCT(num) AS ConsecutiveNums FROM(
    SELECT *, 
    LAG(num) OVER(ORDER BY id) AS prev,
    LEAD(num) OVER(ORDER BY id) AS next
    FROM Logs
) t
WHERE num = prev AND num = next