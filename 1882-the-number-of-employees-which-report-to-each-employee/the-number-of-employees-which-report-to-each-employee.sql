SELECT e.employee_id,
        e.name,
        t.reports_count,
        t.average_age
        FROM Employees e
        JOIN
        (SELECT reports_to, COUNT(*) AS reports_count, ROUND(AVG(age)) AS average_age 
            FROM Employees
            WHERE reports_to IS NOT NULL
            GROUP BY reports_to) t
            ON e.employee_id = t.reports_to
            ORDER BY e.employee_id
