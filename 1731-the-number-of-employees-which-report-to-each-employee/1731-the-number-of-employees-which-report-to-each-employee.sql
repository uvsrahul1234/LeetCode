# Write your MySQL query statement below

SELECT
    e.employee_id,
    e.name,
    COUNT(e1.employee_id) as reports_count,
    ROUND(AVG(e1.age)) as average_age
FROM Employees e
LEFT JOIN Employees e1
ON e.employee_id = e1.reports_to
GROUP BY e.employee_id
HAVING reports_count > 0
ORDER BY e.employee_id