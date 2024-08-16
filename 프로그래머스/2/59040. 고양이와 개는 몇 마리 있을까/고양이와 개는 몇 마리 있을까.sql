-- 코드를 입력하세요
SELECT ANIMAL_TYPE, COUNT(*) count
from animal_ins
group by animal_type
order by animal_type;