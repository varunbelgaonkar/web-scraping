from selenium import webdriver
#driver = webdriver.Chrome(executable_path = r'C:\Users\varunraj\Downloads\chromedriver_win32\chromedriver.exe' )
driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
url = 'https://www.python.org/'
driver.get(url)
page = driver.page_source
print(page)
