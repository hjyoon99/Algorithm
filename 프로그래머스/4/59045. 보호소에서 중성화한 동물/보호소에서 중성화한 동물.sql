-- 중성화 수술을 거친 동물의 정보
-- 보호소 들어와서 중성화
SELECT i.ANIMAL_ID, i.ANIMAL_TYPE, i.NAME FROM ANIMAL_INS i
JOIN ANIMAL_OUTS o
ON i.ANIMAL_ID = o.ANIMAL_ID
-- i에서는 중성화 x, o에서는 중성화 o
WHERE i.SEX_UPON_INTAKE LIKE 'Intact%' AND (o.SEX_UPON_OUTCOME LIKE 'Neutered%' OR  o.SEX_UPON_OUTCOME LIKE 'Spayed%')
ORDER BY i.ANIMAL_ID
