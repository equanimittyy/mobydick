# Read and import local HTML
print('Importing required modules')
from bs4 import BeautifulSoup
import csv

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

# Write to .txt to test the formatting
with open ('Moby-Dick.txt', 'w', encoding='utf-8') as file:
    file.write(title)
    for element in h2_elementlist:
        file.write((element.get_text()))
        for tag in element.next_siblings:
            if tag.name == 'h2':
                break
            else:
                file.write(tag.get_text(strip=True, separator=' '))
print('Moby-Dick transcript has been transcribed')

# Write to .csv
print ('Writing csv file...')
with open ('MobyTable.csv', 'w', encoding='utf-8',newline='') as mobTable:
    csvwriter = csv.writer(mobTable, delimiter=',')
    mobTable.write('\ufeff')
    field = ['Header','Content']
    
    #Write header
    csvwriter.writerow(field)
    
    for element in h2_elementlist:
        for tag in element.next_siblings:
            if tag.name == 'h2':
                break
            else:
                head = element.get_text(strip=True, separator=' ')+ ' '
                cont = tag.get_text(strip=True, separator=' ')
                
                csvwriter.writerow({head,cont})

    print ('MobyTable exported')
        
            



