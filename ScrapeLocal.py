# Read and import local HTML
print('Importing required modules')
from bs4 import BeautifulSoup

print ('Reading file')
with open ('theSoup.html', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'lxml')

## Depreciated code relating to testing whether the soup reads correctly
# Print the soup
#print ('Printing the soup...')
#print (soup.prettify())
#print ('Soup printed')

title = soup.find('h1').get_text()
h2_elementlist = soup.find_all('h2')
print (title)

with open ('Moby-Dick.txt','w',encoding='utf-8') as file:
    file.write(title)
    for element in h2_elementlist:
        file.write((element.get_text()))
        for tag in element.next_siblings:
            if tag.name == 'h2':
                break
            else:
                file.write(tag.get_text(strip=True, separator=' '))
print('Moby-Dick file has been transcribed')
            



