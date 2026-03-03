# Write your MySQL query statement below
Select Email from (
    select email as Email, count(email) as num
    from person
    group by email
) as x
where num > 1;