Example 1:

Input: 
Orders table:
+--------------+-----------------+
| order_number | customer_number |
+--------------+-----------------+
| 1            | 1               |
| 2            | 2               |
| 3            | 3               |
| 4            | 3               |
+--------------+-----------------+
Output: 
+-----------------+
| customer_number |
+-----------------+
| 3               |
+-----------------+
Explanation: 
The customer with number 3 has two orders, which is greater than either customer 1 or 2 because each of them only has one order. 
So the result is customer_number 3.
 

Follow up: What if more than one customer has the largest number of orders, can you find all the customer_number in this case?

#First Solution Subquery

SELECT customer_number
FROM
(
SELECT COUNT(customer_number)As NumOrd, customer_number
FROM Orders 
GROUP BY customer_number
) o
WHERE o.NumOrd = (SELECT MAX(p.NumOrd) FROM(
SELECT COUNT(customer_number)As NumOrd, customer_number
FROM Orders 
GROUP BY customer_number
) p)

# Second solution using Common Table Expressions
WITH cte AS
(
SELECT COUNT(customer_number) As NumOrd, customer_number
FROM Orders 
GROUP BY customer_number
) 

SELECT customer_number
FROM cte 
WHERE NumOrd = (SELECT MAX(NumOrd) FROM cte)