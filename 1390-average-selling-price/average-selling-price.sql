# Write your MySQL query statement below
select
prices.product_id,
case 
when round((sum(prices.price*unitssold.units)/sum(unitssold.units)),2)>0 then round((sum(prices.price*unitssold.units)/sum(unitssold.units)),2)
else 0
end as average_price
from
prices
left join unitssold on (unitssold.purchase_date between prices.start_date and prices.end_date) and prices.product_id=unitssold.product_id
group by
prices.product_id