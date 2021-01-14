from selenium import webdriver
from bs4 import BeautifulSoup

class Film():
	def __init__(self):
		self.rank = ""
		self.title = ""
		self.year = ""
		self.link = ""

film_list = []

def get_movie_details():
	url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
	driver = webdriver.PhantomJS(executable_path=r'C:\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
	driver.get(url)
	page = driver.page_source

	soup = BeautifulSoup(page, 'lxml')
	movies = soup.find('table', class_='chart')
	for td in movies.find_all('td', class_ ='titleColumn'):
		full_title = td.text.strip().replace("\n","").replace('      ',"")
		film = Film()
		film.rank = full_title.split(".")[0]
		film.title = full_title.split(".")[1].split("(")[0]
		film.year = full_title.split("(")[1][:-1]
		film_list.append(film)

	for f in film_list:
		print(f.rank)
		print(f.title)
		print(f.year)

	driver.quit()

	return film_list
	

get_movie_details()



	#print(full_title)
