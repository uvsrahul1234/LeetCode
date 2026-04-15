# Write your MySQL query statement below

-- SELECT
--     max(num) as num
-- FROM MyNumbers
-- WHERE num IN (SELECT
--     num
-- FROM MyNumbers
-- GROUP BY num
-- HAVING COUNT(num) = 1)

SELECT COALESCE((SELECT
    num
FROM MyNumbers
GROUP BY num
HAVING COUNT(num) = 1
ORDER BY num DESC
LIMIT 1), null) as num