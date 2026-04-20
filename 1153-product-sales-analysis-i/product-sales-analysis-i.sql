# Write your MySQL query statement below
select p.product_name,s.price,s.year from sales as s LEFT JOIN Product as p ON s.product_id = p.product_id