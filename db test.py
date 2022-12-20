import sqlite3
import csv
from itertools import product

con = sqlite3.connect(input())
cur = con.cursor()
date, side = input().split()
bays = cur.execute(f'''SELECT title FROM Bays WHERE 
        side_id = (SELECT id FROM Sides WHERE title = ?) ORDER BY title ASC''', (side,)).fetchall()
predictions = cur.execute(f'''SELECT time, waves, wind FROM Predictions WHERE date = ? AND 
        side_id = (SELECT id FROM Sides WHERE title = ?) ORDER BY time ASC''', (date, side,)).fetchall()

with open("weather.csv", mode='w', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    for i in product(bays, predictions):
        writer.writerow([i[0][0], i[1][0], i[1][1], i[1][2]])
