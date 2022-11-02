import psycopg2

username = 'Perederei_Bohdan'
password = 'qwerty123'
database = 'VideoGamesSales'
host = 'localhost'
port = '5432'

query_1 = '''
SELECT plat_name, SUM(copies_sold) as copies_sold 
FROM (gameplatformregionsales INNER JOIN platform  ON  gameplatformregionsales.plat_id = platform.plat_id)
GROUP BY platform.plat_id;
'''

query_2 = '''
SELECT plat_name, COUNT(game_id) as releases
FROM (gameplatform INNER JOIN platform  ON gameplatform.plat_id = platform.plat_id)
GROUP BY platform.plat_id;
'''

query_3 = '''
SELECT release_year, COUNT(game_id) as releases
FROM gameplatform
GROUP BY release_year
ORDER BY release_year;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    print("Total number of sold copies grouped by platform")
    cur = conn.cursor()
    cur.execute(query_1)
    for row in cur:
        print(row)
    print("")

    print("Number of games released on each platform")
    cur = conn.cursor()
    cur.execute(query_2)
    for row in cur:
        print(row)
    print("")

    print("Number of releases each year")
    cur = conn.cursor()
    cur.execute(query_3)
    for row in cur:
        print(row)
    print("")