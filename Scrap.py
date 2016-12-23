# this problem is about web scraping. In this problem a variable takes a url of a webpage and 
# prints the code of "view page source" option in suitable format using .prettify() method.
# for loop prints all the links containing the webpage
# Requests & BeautifulSoup module is used 
# install Requests & BeautifulSoup using command : "pip install requests beautifulsoup4"

import requests
from bs4 import BeautifulSoup

url = "https://www.yelp.com/search?find_desc=Restaurants&find_loc=San+Francisco%2C+CA&ns=1"

src_code = requests.get(url)

src_soup = BeautifulSoup(src_code.text, 'html.parser')
print(src_soup.prettify())

for link in src_soup.findAll('a'):
    print(link)
