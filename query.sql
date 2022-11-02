SELECT plat_name, SUM(copies_sold) as copies_sold 
FROM (gameplatformregionsales INNER JOIN platform  ON  gameplatformregionsales.plat_id = platform.plat_id)
GROUP BY platform.plat_id;

SELECT plat_name, COUNT(game_id) as releases
FROM (gameplatform INNER JOIN platform  ON gameplatform.plat_id = platform.plat_id)
GROUP BY platform.plat_id;

SELECT release_year, COUNT(game_id) as releases
FROM gameplatform
GROUP BY release_year
ORDER BY release_year;