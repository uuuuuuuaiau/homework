import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import datetime

conn = sqlite3.connect('weather_db.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date_time TEXT,
        temperature REAL
    )
''')
conn.commit()

url = 'https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%B6%D0%B8%D1%82%D0%BE%D0%BC%D0%B8%D1%80'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

temperature_element = soup.find('div', {'class': 'main loaded'})
temperature_str = temperature_element.find('p', {'class': 'today-temp'}).text.strip()
temperature = float(temperature_str.replace('°', ''))

date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

cursor.execute('INSERT INTO weather (date_time, temperature) VALUES (?, ?)', (date_time, temperature))
conn.commit()

conn.close()

