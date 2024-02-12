# START of script
print('Web Scraping script executed.')
# import required modules
print ('Importing required modules.')
from bs4 import BeautifulSoup
import requests

website = 'https://www.gutenberg.org/cache/epub/2701/pg2701-images.html'
WebResponse = requests.get(website)
WebContent = WebResponse.text

soup = BeautifulSoup(WebContent, 'lxml')
# Print the soup and export
print ('Printing the soup...')
print (soup.prettify())

with open ('theSoup.html', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())

# END of script
print ('Soup printed and exported to txt')
