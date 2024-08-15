-- 코드를 입력하세요
SELECT left(product_code, 2) CATEGORY, count(*) PRODUCT
from product
group by CATEGORY;