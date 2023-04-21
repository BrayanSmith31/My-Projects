Input: 
Submissions table:
+---------+----------+
| sub_id  || parent_id  | 
+---------+----------+
| 1       || Null       | 
| 2       || Null       |
| 1       || Null       |
| 12      || Null       |
| 3       || 1          |
| 5       || 2          |
| 3       || 1          |
| 4       || 1          |
| 9       || 1          |
| 10      || 2          |
| 6       || 7          |

+---------+----------+
Output: 
+---------+
| post_id || number_of_comments |
+---------+
|   1     || 3     |
|   2     || 2     |
|   12    || 0     |
+---------+

Write an SQL query to find the number of comments per post.The result table shoud contain post_id
and its corresponding number_of_comments.

The Submissions table, may contain duplicate comments. you should count the unique comments 
per post

Note : parent_id is null for post, and will have a post_id for the comments

WITH cte AS
(
SELECT sub_id
FROM Submissions
WHERE parent_id IS Null
)

SELECT post_id, COUNT(DISTINCT sub_id) AS number_of_comments
FROM Submissions
WHERE parent_id IS IN cte
GROUP BY parent_id