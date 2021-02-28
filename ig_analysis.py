from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd
import numpy as np
from collections import Counter


driver = webdriver.Chrome(r'C:\Users\varun\OneDrive\Documents\python projects\chromedriver.exe')

def get_post_links(username):
	url = f"https://www.instagram.com/{username}/"
	driver.get(url)
	driver.implicitly_wait(5)
	
	info = driver.find_elements(By.XPATH, "//li[@class='Y8-fY ']")
	posts = info[0].text
	followers = info[1].text
	following = info[2].text
	
	post_links = []
	while len(post_links)<50:
		links = driver.find_elements(By.XPATH, "//a[contains(@href,'/p/')]")
		for link in links:
			post_links.append(link.get_attribute('href'))
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
		time.sleep(3)
		try:
			driver.find_element(By.XPATH, "//button[@class='tCibT qq7_A  z4xUb w5S7h']").click()
		except NoSuchElementException as e:
			print(e)

	return post_links, posts, followers, following
	

def get_post_info(username):
	hashtags_used = []
	likes_got = []
	post_links, posts, followers, following = get_post_links(username)
	for url in post_links[:10]:
		driver.get(url)
		likes = driver.find_element(By.XPATH, "//div[@class='Nm9Fw']").text.split(" ")[0]
		likes_got.append(int(likes.replace(",","_")))
		#timestamp = driver.find_element(By.XPATH, "//time[@class='_1o9PC Nzb55']").get_attribute("datetime")
		#date = timestamp.split("T")[0]
		#time = 
		hashtags = driver.find_elements(By.XPATH, "//a[@class=' xil3i']")
		hashtag_text = [hashtag.text for hashtag in hashtags]
		hashtags_used.append(hashtag_text)

	df = pd.DataFrame({
		'links': post_links[:10],
		'likes': likes_got,
		'hashtags': hashtags_used
		})
	
	average_likes = df["likes"].mean()
	arr = df["hashtags"].apply(pd.Series).values.ravel()
	count_dict = Counter(arr)	
	del count_dict[np.nan]
	top_5_hashtag = pd.Series(count_dict).nlargest(5)	
	driver.quit()
	return average_likes, top_5_hashtag	,posts, followers, following



	

#post_url = []
#for post in post_links:
#	url_p = post.get_attribute('href')
#	post_url.append(url_p)
#
#print(post_url)
#
#login
#driver.find_element(By.XPATH, "//input[@name='username']").send_keys(username)
#driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
#driver.find_element(By.XPATH, "//button[@class='sqdOP  L3NKy   y3zKF     ']").click()
#time.sleep(3)
#for popup box
#driver.find_element(By.XPATH, "//button[@class='sqdOP  L3NKy   y3zKF     ']").click()
#driver.find_element(By.XPATH, "//button[@class='aOOlW   HoLwm ']").click()
#time.sleep(3)
#searching for pages
#search_box = driver.find_element(By.XPATH, "//div[@class='LWmhU _0aCwM']")
#search_box.click()
#time.sleep(3)
#search_box.send_keys("ml.india")

