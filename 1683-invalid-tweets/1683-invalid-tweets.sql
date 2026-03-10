# Write your MySQL query statement below

SELECT
    tweet_id
FROM Tweets as t
WHERE LENGTH(content) > 15