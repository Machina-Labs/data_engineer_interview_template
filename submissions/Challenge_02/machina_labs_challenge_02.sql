#Write a Query to retrieve the top 5 employees based on sorted hire date. Earlist date being on top in the sort.
select * from machina_labs.employees
order by hire_date asc
limit 5;
#Write a Query to retrieve employees based on Highest Salary.
with CTE_salary_rank
as
(
select employee_id, row_number() over ( order by salary desc) row_id 
from machina_labs.employees
)
select employee_id 
from CTE_salary_rank
where row_id=1;

#Write a query to list the number of jobs available.

select count(distinct job_id) from machina_labs.employees;

#Write a query to get the maximum salary of an employee working as a Programmer.
select max(emp.SALARY) as max_salary_programmer
from machina_labs.employees emp
join machina_labs.jobs jb on emp.job_id=jb.job_id
where jb.JOB_TITLE='Programmer';

#Write a query to get the average salary and number of employees working the department 90.
with dep_90
as (
select * from machina_labs.employees
where DEPARTMENT_ID=90)
select count(*) as number_of_employees
,avg(salary) as average_salary
from dep_90