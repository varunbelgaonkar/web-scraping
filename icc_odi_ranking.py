from selenium import webdriver
from bs4 import BeautifulSoup
import re

class Player():
	def __init__(self):
		self.name = ""
		self.nationality = ""
		self.rating = ""
		self.link = ""

players_list = []

def get_player_details():
 
	url = 'https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting'
	driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
	driver.get(url)
	page = driver.page_source
	#print(page)
	
	soup = BeautifulSoup(page, 'lxml')
	table = soup.find('table', class_ = 'table rankings-table')
	#print(table.prettify())
	player = table.find('tr', class_ = 'rankings-block__banner')
	#details of first ranked player
	name = player.find('div', class_ = 'rankings-block__banner--name-large').text
	nationality = player.find('div', class_ = 'rankings-block__banner--nationality').text.strip()
	rating = player.find('div', class_ = 'rankings-block__banner--rating').text
	link = player.find('a')['href']
	
	first_rank_player = Player()
	first_rank_player.name = name
	first_rank_player.nationality = nationality
	first_rank_player.rating = rating
	first_rank_player.link = link
	
	players_list.append(first_rank_player)
	
	
	#print(name.text)
	#print(nationality.text.strip())
	#print(rating.text)
	#print(link['href'])
	#print(" ")
	
	#details of other ranked players
	players = table.find_all('tr', class_ = 'table-body')
	for player in players:
		name = player.find('a').text
		nationality = player.find('span', class_ = 'table-body__logo-text').text
		rating = player.find('td', class_ = 'table-body__cell rating').text
		link = player.find('a')['href']
	
		player_obj = Player()
		player_obj.name = name
		player_obj.nationality = nationality
		player_obj.rating = rating
		player_obj.link = link
	
		players_list.append(player_obj)	
	
	for one_player in players_list:
		print(one_player.name)
		print(one_player.nationality)
		print(one_player.rating)
		print(one_player.link)
		print("  ")
	
		#print(name)
		#print(nationality)
		#print(rating)
		#print(link)
		#print(" ")
	driver.quit()

	return players_list



	


get_player_details()



