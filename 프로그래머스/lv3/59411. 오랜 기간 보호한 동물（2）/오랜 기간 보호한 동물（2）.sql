-- 코드를 입력하세요
SELECT ANIMAL_OUTS.ANIMAL_ID, ANIMAL_OUTS.NAME
FROM ANIMAL_OUTS
RIGHT JOIN ANIMAL_INS
    ON ANIMAL_OUTS.ANIMAL_ID = ANIMAL_INS.ANIMAL_ID
WHERE
    ANIMAL_OUTS.ANIMAL_ID IS NOT NULL
ORDER BY
    DATEDIFF(ANIMAL_OUTS.DATETIME, ANIMAL_INS.DATETIME) DESC
LIMIT 2;
    