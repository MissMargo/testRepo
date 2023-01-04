select count(distinct JOB_ID) from employees;
select avg (salary),count(*) from employees where DEPARTMENT_ID = 90;
select job_id, count(*) from employees group by job_id;
select a.first_name, a.last_name, a.department_id, b.department_name
from employees a join departments b on a.department_id = b.department_id;
select a.first_name, a.last_name, a.job_id, a.department_id
from employees a join departments b on a.DEPARTMENT_ID = b.DEPARTMENT_ID join locations c on b.LOCATION_ID = c.LOCATION_ID
where c.city = 'London';