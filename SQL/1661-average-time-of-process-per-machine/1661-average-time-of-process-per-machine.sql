# Write your MySQL query statement below

-- SELECT
--     a1.machine_id,
--     ROUND(AVG((a2.timestamp - a1.timestamp)),3) AS processing_time
-- FROM activity AS a1
-- JOIN activity AS a2
-- ON a1.machine_id = a2.machine_id
-- AND a1.process_id = a2.process_id
-- AND a1.timestamp < a2.timestamp
-- GROUP BY a1.machine_id

select a1.machine_id, round(avg(a2.timestamp-a1.timestamp),3)
as processing_time
from activity a1 join activity a2
on a1.machine_id = a2.machine_id
and a1.process_id = a2.process_id
and a1.activity_type = 'start'
and a2.activity_type = 'end'
group by a1.machine_id