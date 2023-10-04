SELECT A.CAR_ID, C.CAR_TYPE, ROUND(((30 * A.DAILY_FEE) * (100-C.DISCOUNT_RATE)/100)) AS FEE
FROM CAR_RENTAL_COMPANY_CAR A JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY B
ON A.CAR_ID = B.CAR_ID
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN C
ON A.CAR_TYPE = C.CAR_TYPE
WHERE A.CAR_ID NOT IN (SELECT CAR_ID FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY WHERE START_DATE < '2022-12-1' AND END_DATE >'2022-11-01') AND C.DURATION_TYPE = '30일 이상'
GROUP BY A.CAR_ID
HAVING C.CAR_TYPE IN('세단', 'SUV') AND (FEE BETWEEN 500000 AND 2000000)
ORDER BY FEE DESC, A.CAR_TYPE, A.CAR_ID DESC