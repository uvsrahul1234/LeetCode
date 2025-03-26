# Write your MySQL query statement below

SELECT 
    id
FROM weather AS w
WHERE temperature > (
    SELECT 
        temperature 
    FROM weather AS w1 
    WHERE w.recordDate = w1.recordDate + 1
) OR temperature > (
    SELECT 
        temperature 
    FROM weather AS w1 
    WHERE w.recordDate + 1 = w1.recordDate
)