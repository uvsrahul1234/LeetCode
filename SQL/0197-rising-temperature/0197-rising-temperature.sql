SELECT
    w2.id
FROM weather AS w1
JOIN weather AS w2
-- ON w1.recordDate - w2.recordDate = -1 <doesn't work as the date could be 31 and 1>
ON DATEDIFF(w1.recordDate, w2.recordDate) = -1
WHERE w2.temperature > w1.temperature

-- SELECT w1.id 
-- FROM Weather w1, Weather w2
-- WHERE w1.recordDate = w2.recordDate + INTERVAL 1 DAY
-- AND w1.temperature > w2.temperature