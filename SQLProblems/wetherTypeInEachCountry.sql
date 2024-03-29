Example:

Input: 
Countries table:
+----+-------+--------+-----------+
| country_id | country_name | 
+----+-------+--------+-----------+
| 2          | USA          |
| 3          | Australia    |
| 7          | Peru         | 
| 5          | China        | 
| 8          | Marocco      |
| 9          | Spain        | 

+----+-------+--------+-----------+
Weather table:
+----+-------+--------+-----------+
| country_id |weather_state | day          | 
+----+-------+--------+-----------+
| 2          | 15           | 2019-11-01   | 
| 2          | 12           | 2019-10-28   | 
| 2          | 12           | 2019-10-27   | 
| 3          | -2           | 2019-11-10   | 
| 3          | 0            | 2019-11-11   | 
| 3          | 3            | 2019-11-12   | 
| 5          | 16           | 2019-11-07   | 
| 5          | 18           | 2019-11-09   | 
| 5          | 21           | 2019-11-23   | 
| 7          | 25           | 2019-11-28   | 
| 7          | 22           | 2019-12-01   | 
| 7          | 29           | 2019-12-02   | 
| 8          | 25           | 2019-11-05   | 
| 8          | 27           | 2019-11-15   | 
| 8          | 31           | 2019-11-25   | 
| 9          | 7            | 2019-10-23   | 
| 9          | 3            | 2019-12-23   | 

+----+-------+--------+-----------+

Output: 
+----------++----------+
| country_name |  weather_type|
+----------+
| USA          | Cold         |
| Australia    | Cold         |
| Peru         | Hot          |
| Marocco      | Hot          |
| China        | Warm         |

+----------

Write an SQL query to find the type of wether in each country for November 2019
the type of where is:
- Cold if the average wether_state is less than or equal to 15
- Hot if the average wether_state is greater than or equal to 25
- Warm otherwise
