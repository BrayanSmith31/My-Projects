Example 1:

Input: 
Cinema table:
+----+-------+
| seat_id | free  |
+----+-------+
| 1       | 1   |
| 2       | 0   |
| 3       | 1   |
| 4       | 1   |
| 5       | 1   |
+----+-------+
Output:
+----+------------+
| seat_id | 
+----+------------+
| 3  | 
| 4  |
| 5  |
+----+------------+
SELECT w.seat_id
FROM
(
    SELECT *, LEAD(free) OVER(
        ORDER BY seat_id
    ) AS Next_seat , LAG(free) OVER(
        ORDER BY seat_id
    ) AS Previous_seat
)
FROM Cinema) AS w
WHERE (w.free=1 AND w.Next_seat=1) OR (w.free=1 AND w.Previous_seat=1)
ORDER BY w.seat_id