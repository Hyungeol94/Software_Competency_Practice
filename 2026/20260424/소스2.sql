-- https://school.programmers.co.kr/learn/courses/30/lessons/301647
-- 부모의 형질을 모두 가지는 대장균 찾기

SELECT e.ID, e.GENOTYPE, p.GENOTYPE as PARENT_GENOTYPE 
FROM ECOLI_DATA AS e JOIN ECOLI_DATA AS p ON e.PARENT_ID = p.ID
WHERE p.GENOTYPE | e.GENOTYPE = e.GENOTYPE
ORDER BY ID ASC