# Write your MySQL query statement below

SELECT
    e.name,
    b.bonus
FROM employee as e
LEFT JOIN bonus as b
ON e.empid = b.empid
WHERE b.bonus IS NULL OR b.bonus < 1000