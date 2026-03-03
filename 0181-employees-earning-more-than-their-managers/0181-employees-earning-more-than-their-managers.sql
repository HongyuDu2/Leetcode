# Write your MySQL query statement below
select employee.name as employee
from employee
join employee as manager
on employee.managerID = manager.id
where employee.salary > manager.salary;