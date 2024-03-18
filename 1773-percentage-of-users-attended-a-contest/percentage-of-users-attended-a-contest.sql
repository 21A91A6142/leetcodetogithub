# Write your MySQL query statement below
select
register.contest_id,
round(((count((users.user_id))/(select count(*) from users))*100),2) as percentage
from
register
left join users on users.user_id=register.user_id
group by
register.contest_id
order by
percentage desc,
register.contest_id asc
