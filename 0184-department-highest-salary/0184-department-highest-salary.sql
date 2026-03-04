# Write your MySQL query statement below
Select
    e.name as Employee,
    e.salary as Salary,
    d.name as Department
From Employee e
Join Department d on e.departmentId = d.id
where e.salary = (
    select Max(salary)
    From Employee
    where departmentId = e.departmentId
);