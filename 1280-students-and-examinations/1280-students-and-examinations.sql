# Write your MySQL query statement below

SELECT
    s.student_id,
    s.student_name,
    sj.subject_name,
    COUNT(e.student_id) as attended_exams
FROM Students as s
CROSS JOIN Subjects as sj
LEFT JOIN Examinations as e
ON s.student_id = e.student_id
AND sj.subject_name = e.subject_name
GROUP BY s.student_id, s.student_name, sj.subject_name
ORDER BY s.student_id, s.student_name