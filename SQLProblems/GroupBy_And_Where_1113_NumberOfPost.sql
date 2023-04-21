Input: 
Actions table:
+-------------+-----------+---------+------------+--------------+
|user_id | post_id | action_date| action  | extra  |
+-------------+-----------+---------+------------+--------------+
| 1      | 1       | 2019-07-01 | view    | null   |
| 1      | 1       | 2019-07-01 | like    | null   |
| 1      | 1       | 2019-07-01 | share   | null   |
| 2      | 4       | 2019-07-04 | view    | null   |
| 2      | 4       | 2019-07-04 | report  | spam   |
| 3      | 4       | 2019-07-04 | view    | null   |
| 3      | 4       | 2019-07-04 | report  | spam   |
| 4      | 3       | 2019-07-02 | view    | null   |
| 4      | 3       | 2019-07-02 | report  | spam   |
| 5      | 2       | 2019-07-04 | view    | null   |
| 5      | 2       | 2019-07-04 | report  | racism |
| 5      | 5       | 2019-07-04 | view    | null   |
| 5      | 5       | 2019-07-04 | report  | racism |

+-------------+-----------+---------+------------+--------------+
Output: 
+-------------+------------+---------+
| report_reason | report_count | 
+-------------+------------+---------+
| spam          |      1       | 
| racism        |      2       | 

Explanation: Note that  we only care about report reasons with non-zero number of reports

Write an sql query that reports number of posts reported yestarday for each reason. Assume today
is 2019-07-05

SELECT extra AS report_reason,COUNT(DISTINCT post_id) AS report_count
FROM Actions
WHERE extra is not null AND action_date='2019-07-04' AND action = 'report'
GROUP BY extra