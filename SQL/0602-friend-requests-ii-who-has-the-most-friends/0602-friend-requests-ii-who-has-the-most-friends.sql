# Write your MySQL query statement below

SELECT ids as id, COUNT(*) AS num
   FROM
   (
        SELECT requester_id AS ids FROM requestaccepted
        UNION ALL
        SELECT accepter_id FROM requestaccepted
    ) AS tmp
GROUP BY ids
ORDER BY num DESC
LIMIT 1
;