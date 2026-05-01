    SELECT ROUND(COUNT(DISTINCT a.player_id)/COUNT(DISTINCT b.player_id),2) as fraction 
    FROM (
        SELECT player_id, MIN(event_date) AS first_login,
        MIN(event_date) + INTERVAL 1 DAY AS expected_day 
        FROM Activity 
        GROUP BY player_id) b
        LEFT JOIN Activity a ON a.player_id = b.player_id 
        AND a.event_date = b.expected_day
