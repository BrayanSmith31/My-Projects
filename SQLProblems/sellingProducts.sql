Write an SQL query to find the average selling price for each product.
average_price should be rounded to 2 decimal places

Input: 
Prices table:
+----+-------+--------+-----------+
| product_id | start_date | end_date    | price |
+----+-------+--------+-----------+
| 1          | 2019-02-17 | 2019-02-28  | 5     |
| 1          | 2019-03-01 | 2019-03-22  | 20    |
| 2          | 2019-02-01 | 2019-02-20  | 15    |
| 2          | 2019-02-21 | 2019-03-31  | 30    |
+----+-------+--------+-----------+
UnitsSold table:
+----+-------+--------+-----------+
| product_id |purchase_date | units| 
+----+-------+--------+-----------+
| 1          | 2019-02-25   | 100  | 
| 1          | 2019-03-01   | 15   | 
| 2          | 2019-02-10   | 200  | 
| 2          | 2019-03-22   | 30   | 
+----+-------+--------+-----------+

Output: 
+----------++----------+
| product_id |  average_price|
+----------+
| 1          | 6.96      |
| 2          | 16.96     |
+----------

SELECT ROUND(SUM(p.price*u.units)/SUM(u.units),2) AS average_price
FROM Prices p
INNER JOIN UnitsSold u ON p.product_id = u.product_id
WHERE u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id