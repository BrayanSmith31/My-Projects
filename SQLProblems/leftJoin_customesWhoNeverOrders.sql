Example 1:

Input: 
Customers table:
+----+-------+
| id | name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Orders table:
+----+------------+
| id | customerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
Output: 
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+

SELECT c.name AS customers
FROM Customers c
LEFT JOIN Orders o
ON c.id = o.customerId
WHERE o.customerId is Null


Another way to solve the problem

SELECT c.name AS Customers
FROM Customers c
WHERE c.id NOT IN 
    (SELECT c.id
    FROM Customers c
    INNER JOIN Orders o
    ON c.id = o.customerId)