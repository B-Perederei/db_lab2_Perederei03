import psycopg2
import matplotlib.pyplot as plt

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
figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)

with conn:
    platform = []
    copies_sold = []

    cur = conn.cursor()
    cur.execute(query_1)
    for row in cur:
        platform.append(row[0])
        copies_sold.append(row[1])
    
    x_range = range(len(platform))
 
    bar_ax.bar(x_range, copies_sold, label='Millions of copeis sold')
    bar_ax.set_title('Total number of sold copies grouped by platform (in millions)')
    bar_ax.set_xlabel('Platform')
    bar_ax.set_ylabel('Millions of copeis')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(platform)
    

with conn:
    platform = []
    games_released = []

    cur = conn.cursor()
    cur.execute(query_2)
    for row in cur:
        platform.append(row[0])
        games_released.append(row[1])
    
    pie_ax.pie(games_released, labels=platform, autopct='%2.2f%%')
    pie_ax.set_title("Number of games released on each platform")

with conn:
    year = []
    games_released = []

    cur = conn.cursor()
    cur.execute(query_3)
    for row in cur:
        year.append(row[0])
        games_released.append(row[1])
    
    graph_ax.plot(year, games_released, marker='o')
    graph_ax.set_xlabel('Year of release')
    graph_ax.set_ylabel('Number of games released')
    graph_ax.set_title('Number of releases each year')

    for y, g_r in zip(year, games_released):
        graph_ax.annotate(g_r, xy=(y, g_r), xytext=(7, 2), textcoords='offset points') 
    

mng = plt.get_current_fig_manager()
mng.resize(1400, 600)

plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.4,
                    hspace=0.4)
                    
plt.show()