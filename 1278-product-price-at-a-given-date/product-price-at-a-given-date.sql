SELECT p.product_id, COALESCE(x.new_price,10) AS price
FROM
    (SELECT DISTINCT product_id FROM Products) as p
    LEFT JOIN
    (SELECT product_id,new_price 
    FROM
        (SELECT product_id,new_price,
        ROW_NUMBER() OVER(PARTITION BY product_id ORDER BY change_date DESC) as rn
        FROM Products 
        WHERE change_date <= '2019-08-16'
        ) t
    WHERE rn = 1) x
ON p.product_id = x.product_id

