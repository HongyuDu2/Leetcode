# Write your MySQL query statement below
Select w1.id 
From Weather w1
join Weather w2
on w2.recordDate = Date_sub(w1.recordDate, Interval 1 day)
where w1.temperature > w2.temperature