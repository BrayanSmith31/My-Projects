Write a SQL query to report for evey three line segments whether they  can form a triangle.

Triangle table:
+----+-------+--------+-----------+
| x  | y  | z  |
+----+-------+--------+-----------+
| 13 | 15 | 30 |
| 10 | 20 | 15 |
+----+-------+--------+-----------+
Output: 
| x  | y  | z  | triangle  |
+----+-------+--------+-----------+
| 13 | 15 | 30 |   No      |
| 10 | 20 | 15 |   Yes     |

SELECT x, y, z 
FROM Triangle
WHERE x+y > z OR x+z > y OR z+y > x