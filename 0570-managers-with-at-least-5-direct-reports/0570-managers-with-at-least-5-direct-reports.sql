# Write your MySQL query statement below

WITH report_count AS(
    SELECT managerId
    FROM Employee
    Group by managerId
    HAVING count(id) >= 5
)
SELECT name
FROM Employee
WHERE id IN (SELECT managerId FROM report_count)