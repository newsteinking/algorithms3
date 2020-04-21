#There is a table courses with columns: student and class
#Please list out all classes which have more than or equal to 5 students.

# Write your MySQL query statement below
SELECT class FROM courses GROUP BY class
HAVING COUNT(DISTINCT student) >= 5