# Write your MySQL query statement below
select x,y,z,
case 
    when x+y>z and y+z>x and x+z>y  then "Yes"
    Else "No"
end as triangle
from Triangle