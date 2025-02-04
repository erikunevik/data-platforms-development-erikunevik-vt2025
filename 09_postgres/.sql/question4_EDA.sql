

-- A)
SELECT
    Utbildningsnamn,
    "utbildningsanordnare administrativ enhet"
FROM myh_2024
WHERE  Utbildningsnamn ILIKE 'Data engineer';

-- B)
SELECT
    Utbildningsnamn,
    Beslut,
    "utbildningsanordnare administrativ enhet"
FROM myh_2024
WHERE Utbildningsnamn ILIKE 'Data engineer' AND Beslut = 'Beviljad';

-- C)

SELECT
    COUNT(utbildningsnamn) AS Utbildning,
    utbildningsområde
FROM myh_2024
GROUP BY utbildningsområde
ORDER BY Utbildning DESC;

--D)

SELECT 
    COUNT(utbildningsnamn) AS Utbildning,
    kommun
FROM myh_2024
GROUP BY kommun
ORDER BY Utbildning DESC;

E) Calculate the percentage of approved programs within each education category.

SELECT
    utbildningsområde,
    COUNT(CASE WHEN Beslut = 'Beviljad' THEN 1 END) AS approved_programs,
    ROUND(
        (COUNT(CASE WHEN Beslut = 'Beviljad' THEN 1 END) * 100.0) / COUNT(*), 
        2
    ) AS approval_percentage
FROM myh_2024
GROUP BY utbildningsområde
ORDER BY approval_percentage DESC;





