SELECT user_id, COUNT(*) AS followers_count
FROM followers 
GROUP BY user_id