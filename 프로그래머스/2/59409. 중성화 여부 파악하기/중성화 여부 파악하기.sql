-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME,
if (sex_upon_intake in ('Neutered Male', 'Spayed Female'), 'O', 'X') 중성화
FROM ANIMAL_INS;