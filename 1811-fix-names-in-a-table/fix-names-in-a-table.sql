# Write your MySQL query statement below
select
user_id,
concat(ucase(left(name,1)),lcase(right(name,length(name)-1))) as name
from
users
order by
user_id