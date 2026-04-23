# Write your MySQL query
SELECT t.machine_id, ROUND(AVG(t.end_time - t.start_time),3) AS processing_time
 FROM
    (SELECT a.machine_id, a.process_id, a.timestamp AS start_time, a1.timestamp AS end_time from Activity AS A 
    JOIN activity AS A1 
    ON A.machine_id = A1.machine_id AND
     A.process_id = A1.process_id 
     WHERE A.activity_type = 'start' AND A1.activity_type = 'end') t 
    GROUP BY t.machine_id