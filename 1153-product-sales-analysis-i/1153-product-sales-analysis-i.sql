# Write your MySQL query statement below
SELECT product_name,year,price
FROM product
RIGHT JOIN sales
ON product.product_id=sales.product_id;