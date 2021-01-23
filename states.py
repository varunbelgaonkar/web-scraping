import requests
from bs4 import BeautifulSoup
import json
import time

class States():
	def __init__(self):
		self.name = " "
		self.link = " "

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
'accept':'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
'accept-encoding':'gzip, deflate, br',
'accept-language':'en-US,en;q=0.9'
}

def get_state_info(headers):
	url = 'https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India'
	r = requests.get(url, headers = headers)
	if r.status_code == 200:
		soup = BeautifulSoup(r.text, 'lxml')
		table = soup.find('table', class_ = ['wikitable','sortable','plainrowheaders','jquery-tablesorter'])
		states = table.find('tbody').find_all('tr')
		states_array = []
	
		for state in states[1:]:
			states_object = States()
			states_object.name = state.find('th', attrs = {'scope' : 'row'}).text.strip()
			states_object.link = state.find('th', attrs = {'scope' : 'row'}).a['href']
			states_array.append(states_object)
		
		#for s in states_array:
		#	print(s.link)
		#	print(s.name)
			
		#	print('https://en.wikipedia.org'+s.link)
		#	print(" ")
	return states_array


def get_additional_info(states_array):

	states_json = []
	for s in states_array:
		url = 'https://en.wikipedia.org'+s.link			
		r = requests.get(url, headers = headers)
		#print(url)
		#print(r.status_code)
		
		if r.status_code == 200:
			soup = BeautifulSoup(r.text, 'lxml')
			table = soup.find('table', class_ = ['infobox', 'geography', 'vcard'])
			tr_tags = table.find_all('tr', class_ = 'mergedrow')
			for d in tr_tags:
				if (d.find('th', attrs = {'scope':'row'})) and (d.find('th', attrs = {'scope':'row'}).a is not None) and (d.find('th', attrs = {'scope':'row'}).a.text == 'Districts'):
					if d.find('td').a is not None:
						#print(d.find('td').a.text)
						districts = d.find('td').a.text
					else:
						#print(d.find('td').text)
						districts = d.find('td').text

				if (d.find('th', attrs = {'scope':'row'}) is not None) and (d.find('th', attrs = {'scope':'row'}).text == ' • Total'):
					#print(d.find('td').text)
					total_area = d.find('td').text.split("(")[0]
					break


					
		#print(s.name)
		#print("Districts: ",districts)
		#print("Total_area: ",total_area)
		#print(s.link)
				

		states_json_object = {
		"State" : s.name,
		"Districts" : districts,
		"Total_area" : total_area,
		"Link" : s.link
		}

		states_json.append(states_json_object)

		time.sleep(4)

	with open('States.json', 'w') as f:
		json.dump(states_json, f)




get_additional_info(get_state_info(headers))


			#for d in tr_tags:
			#	if (d.find('th', attrs = {'scope':'row'}) is not None) and (d.find('th', attrs = {'scope':'row'}).text == ' • Total'):
			#		#print(d.find('td').text)
			#		add_info.append(d.find('td').text)
			#		print(add_info)




		
				
							

					#if (d.find('th', attrs = {'scope':'row'}).a is not None) and (d.find('th', attrs = {'scope':'row'}).a.text == 'Districts'):
					#	num_of_districts = d.find('td').text
					#	print(num_of_districts)

	

#get_state_info(headers)














		




