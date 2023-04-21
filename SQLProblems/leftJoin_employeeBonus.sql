Example 1:

Input: 
Employee table:
+----+-------+---------------------------
| empId | name  | supervisor  | salary  |
+----+-------+---------------------------
| 3     | Brand | null        | 4000    |
| 1     | Jhon  | 3           | 1000    |
| 2     | Dan   | 3           | 2000    |
| 4     | Thomas| 3           | 4000    |

Bonus table:
+----+-------+----
| empId | Bonus  |
+----+-------+---- 
| 2     | 500    | 
| 4     | 2000   | 

+----+-------+
Output:
+----+-------+----
| name  | Bonus  |
+----+-------+---- 
| Bran  | Null   | 
| Jhon  | Null   | 
| Dan   | 500    | 
| Thomas| 2000   | 
+----+------------+

SELECT e.name, b.bonus
FROM Employee e
LEFT JOIN Bonus b 
ON empId
WHERE b.Bonus < 1000 OR b.Bonus IS NUll