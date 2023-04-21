Example 1:

Input: 
MyNumbers table:
+---------+----------+
| num     | 
+---------+----------+
| 8       | 
| 8       | 
| 3       | 
| 3       | 
| 1       | 
| 4       | 
| 5       | 
| 6       | 
+---------+----------+
Output: 
+---------+
| num   |
+---------+
|   6   |
+---------+

A single number is a number that appeared only once in the MyNumbers table.

Write a SQL query to report the largest single number. if there is no silge number return null

WITH cte AS (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
)
SELECT 
CASE
    WHEN COUNT(*)>0 THEN MAX(num)
    ELSE null
END AS num
FROM cte