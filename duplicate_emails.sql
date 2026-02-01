# Write your MySQL query statement below
SELECT email AS Email
FROM Person
Group by email
Having count(*) > 1;