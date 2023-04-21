Example: 

Input:
Point Table 
+----------+
| X |
+----------+
|-1 |
| 0 |
| 2 |
+----------+
Output:
| shortest |
+----------+
|    1     |

Explanation: The shortest distance is between -1 y 0 which is 1 

Follow up: How can you optimize your query if Point table is sorted in ascending order?

SELECT MIN(ABS(x.p1-x.p2)) AS shortest
FROM Point p1
CROSS JOIN Point p2
WHERE x.p1 <> x.p2
