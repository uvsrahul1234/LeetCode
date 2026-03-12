# Write your MySQL query statement below
SELECT
    w1.id
FROM Weather as w
LEFT JOIN Weather as w1
ON DATEDIFF(w.recordDate, w1.recordDate) = -1
WHERE w1.temperature > w.temperature