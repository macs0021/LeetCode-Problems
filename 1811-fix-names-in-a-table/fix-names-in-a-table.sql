SELECT user_id, CONCAT(UPPER(LEFT(name, 1)), LOWER(RIGHT(name,LEN(name)-1))) AS name
FROM users
ORDER BY user_id