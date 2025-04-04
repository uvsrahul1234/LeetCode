# Write your MySQL query statement below

SELECT 
    customer_id,
    COUNT(visit_id) AS count_no_trans
FROM visits
WHERE visit_id NOT IN (
    Select DISTINCT
        visit_id 
    FROM transactions
)
GROUP BY customer_id
