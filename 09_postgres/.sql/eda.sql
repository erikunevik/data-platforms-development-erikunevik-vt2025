SELECT * FROM myh_2024;

-- SELECT
--     utbildningsnamn,
--     utbildningsområde,
--     "yh-poäng",
--     beslut,
--     "utbildningsanordnare administrativ enhet",
--     kommun
-- FROM
--     myh_2024
-- WHERE
--     beslut = 'Beviljad'
--     AND utbildningsområde = 'Data/IT';

-- SELECT
--     COUNT(*) AS total_applied
-- FROM
--     it_educations;

-- SELECT 
--     * 
--     FROM 
--     it_educations 
-- WHERE utbildningsnamn LIKE "%data eng%";

-- WITH
--     approved AS (
--         SELECT
--             COUNT(*) AS count
--         FROM
--             it_educations
--         WHERE
--             beslut = 'Beviljad'
--     ),
--     total AS (
--         SELECT
--             COUNT(*) AS count
--         FROM
--             it_educations
--     )
-- SELECT
--     approved.count,
--     total.count,
--     CAST(approved.count AS NUMERIC) / total.count
-- FROM
--     approved,
--     total