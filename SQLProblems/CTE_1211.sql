Input: 
Queries table:
+-------------+-----------+---------+------------+--------------+
|query_name|     result    |position|rating| 
+-------------+-----------+---------+------------+--------------+
| Dog      | dog_name_1    | 1      | 5    | 
| Dog      | dog_name_2    | 2      | 5    | 
| Dog      | dog_name_3    | 200    | 1    | 
| Cat      | cat_name_1    | 5      | 2    | 
| Cat      | cat_name_2    | 3      | 3    | 
| Cat      | cat_name_3    | 7      | 4    | 
+-------------+-----------+---------+------------+--------------+
Output: 
+-------------+------------+---------+
| query_name  | quality | poor_query_percentage|
+-------------+------------+---------+
| Dog         | 2.50    | 33.33                |
| Cat         | 0.66    | 33.33                |
+-------------+------------+---------+

Explanation: 
Dog query quality is ((5/1 + 5/2 + 1/200)/3) = 2.50
Cat query quality is ((2/5 + 3/3 + 4/7)/3) = 0.66

Dog poor_query_percentage is (1/3)*100 = 33.33 Percentage of rating less than 3
Cat poor_query_percentage is (1/3)*100 = 33.33 Percentage of rating less than 3

Both quality and Percentage should be rounded to two decimal places

WITH cte AS
(
SELECT query_name, rating/position AS ratio, 
    CASE
        WHEN rating < 3 THEN 1
        ELSE 0 
        END AS poor_query_binary
FROM Queries
)

SELECT query_name, ROUND(AVG(ratio),2) AS quality,
ROUND((SUM(poor_query_binary)/COUNT(*))*100,2) AS poor_query_percentage 
FROM cte
GROUP BY query_name


