import pandas as pd
import requests
from bs4 import BeautifulSoup


page = requests.get('https://forecast.weather.gov/MapClick.php?lat=38.8904&lon=-77.032#.XnQCAYhKjD4')
soup = BeautifulSoup(page.content, 'html.parser')

#
week = soup.find(id='seven-day-forecast-body')

items = (week.find_all(class_='tombstone-container'))

#list for the 



#for i in range(len(name)):
#	print(name[i], desc[i], temp[i])

name = [item.find(class_='period-name').get_text() for item in items]
desc = [item.find(class_='short-desc').get_text() for item in items]
temp = [item.find(class_='temp').get_text() for item in items]


weather = pd.DataFrame(
	{'period': name,
	'description': desc,
	'temp': temp

	})

print(weather)
#weather.to_csv('results.csv', sep=';')