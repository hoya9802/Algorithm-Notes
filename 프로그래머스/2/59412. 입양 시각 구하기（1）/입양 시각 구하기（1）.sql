-- 코드를 입력하세요
SELECT HOUR(datetime) as HOUR, count(*) COUNT
from animal_outs
where time_format(datetime, '%H:%i') between '09:00' and '19:59'
group by HOUR(datetime)
order by HOUR;