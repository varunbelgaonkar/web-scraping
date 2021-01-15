from bs4 import BeautifulSoup
import requests

#creating a csv file
filename = "components.csv"
f = open(filename,'w') 
headers = "Product_name, Price\n"
f.write(headers)

url = 'https://www.electronicscomp.com/sensors-module/modules/gsm-gps-module'
page = requests.get(url)   #Getting the reponse from web page
if page.status_code == 200:    #checking if the request is successful
  soup = BeautifulSoup(page.content, 'html.parser')
  product_container = soup.find_all('div', class_ = 'product-layout product-list col-xs-12')
  for product in product_container:
    product_name = product.find('div', class_ = 'styleh4categ').string
    price = product.find('div', class_ = 'price-tab-main').find('div', class_ = 'price').span.string
    print("Product_name: " + product_name)
    print("Price: " + price)
    f.write(product_name + "," + price + "\n")

f.close()















