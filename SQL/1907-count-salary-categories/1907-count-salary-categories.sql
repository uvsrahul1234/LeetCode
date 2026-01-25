# Write your MySQL query statement below

SELECT
    IF(COUNT(*) IS NOT NULL, 'Low Salary',0) AS category,
    COUNT(*) AS accounts_count
FROM Accounts
WHERE income < 20000
UNION
SELECT
    IF(COUNT(*) IS NOT NULL, 'Average Salary', 0) AS category,
    COUNT(*) AS accounts_count
FROM Accounts
WHERE income >= 20000 AND income <=50000
UNION
SELECT
    IF(COUNT(*) IS NOT NULL, 'High Salary',0) AS category,
    COUNT(*) AS accounts_count
FROM Accounts
WHERE income > 50000