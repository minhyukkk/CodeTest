-- 코드를 입력하세요
SELECT C.APNT_NO, A.PT_NAME, A.PT_NO, C.MCDP_CD, B.DR_NAME, C.APNT_YMD
FROM APPOINTMENT C JOIN PATIENT A
ON C.PT_NO = A.PT_NO
JOIN DOCTOR B
ON C.MDDR_ID = B.DR_ID
WHERE DATE_FORMAT(C.APNT_YMD, '%Y-%m-%d') = '2022-04-13' AND C.MCDP_CD = 'CS' AND C.APNT_CNCL_YN = 'N'
ORDER BY C.APNT_YMD 