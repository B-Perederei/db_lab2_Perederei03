INSERT INTO 
Game(game_id, game_name, game_genre, game_publisher)
VALUES
(1, 'Call of Duty: Modern Warfare 2', 'Shooter', 'Activision'),
(2, 'Grand Theft Auto IV', 'Action', 'Take-Two Interactive'),
(3, 'Battlefield 3', 'Shooter', 'Electronic Arts'),
(4, 'Need for Speed Underground 2', 'Racing', 'Electronic Arts'),
(5, 'The Elder Scrolls V: Skyrim', 'Role-Playing', 'Bethesda Softworks'),
(6, 'Medal of Honor: Frontline', 'Shooter', 'Electronic Arts');

INSERT INTO 
Platform(plat_id, plat_name)
VALUES
('X360', 'Xbox 360'),
('PS4', 'Playstation 4'),
('PS3', 'Playstation 3'),
('PS2', 'Playstation 2'),
('PC', 'Personal computer');

INSERT INTO 
Region(region_id, region_name)
VALUES
('NA', 'North America'),
('SA', 'South America'),
('EU', 'European Union'),
('JP', 'Japan'),
('OTHER', 'Other regions');

INSERT INTO 
GamePlatform(game_id, plat_id, release_year)
VALUES
(1, 'X360', 2009),
(1, 'PS3', 2009),
(2, 'X360', 2008),
(2, 'PS3', 2008),
(3, 'X360', 2011),
(3, 'PS3', 2011),
(4, 'PS2', 2004),
(5, 'X360', 2011),
(5, 'PS3', 2011),
(6, 'PS2', 2002);

INSERT INTO
GamePlatformRegionSales(game_id, plat_id, region_id, date_counted, copies_sold)
VALUES
(1, 'X360', 'NA', '2016-12-22', 8.52),
(1, 'PS3', 'EU', '2016-12-22', 3.64),
(1, 'PS3', 'JP', '2016-12-22', 0.38),
(2, 'PS3', 'JP', '2016-12-22', 0.44),
(2, 'X360', 'NA', '2016-12-22', 6.76),
(3, 'PS3', 'NA', '2016-12-22', 2.85),
(4, 'PS2', 'EU', '2016-12-22', 3.02),
(5, 'PS3', 'JP', '2016-12-22', 0.25),
(5, 'X360', 'EU', '2016-12-22', 2.79),
(6, 'PS2', 'NA', '2016-12-22', 2.93);

