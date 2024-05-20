## Introduction:
This project was created with the intention to expose myself to technical challenges to further my technical skills in 
a self-directed ETL/ELT process. Overall, I sought to assess my adaptability to unfamiliar technologies and gain a deeper 
understanding in what might be involved in processing semi-unstructured data.


## Discussion:

### Data Scraping using Python -
Using BeautifulSoup4, I had created a simple WebScrape.py script that imports/loads the BeautifulSoup module, and obtains the
HTML data from 'https://www.gutenberg.org/cache/epub/2701/pg2701-images.html', which contained text for the novel "Moby Dick".

Following this, it exported a local HTML copy of the novel so that it might be used by my second script ScrapeLocal.py to
convert the HTML data into a usable format for MySQL (.csv).

I had made this a two step process (to obtain the data and convert the HTML data) so as to not sent too many web requests to the 
live website in my attempts to write a script that would suit my needs.

### Using MySQL to obtain tables -
Following the conversion of the HTML data into a usable .csv format (MobyTable.csv), I had imported this into a local instance
of MySQL (localhost:3306) where I applied direct modifications to the table to create a primary key 'id_index' and an 'isActive'
column to attempt to transform the data and remove issues with the extraction of data from HTML.

For example, the 'Header' column contained non-header data due to the way the elements in HTML were structured. I had utilised an
'isActive' column in an attempt to remove erronous data with middling success. In retrospect, I believe the most efficient way to
have cleaned/transform data would have been in Python rather than in SQL, where I would have then used clean data to transform 
and create the tables I required for visualisation.

The transformation of data in SQL, particularly to delimit the 'content' column and seperate the individual words was a
difficult challenge. However, through practical experience gained through exercises on StrataScratch, I used my new
founded skills to utilise the 'substring_index()' function and a common table expression "CTE" as the basis of the solution to 
my predicament. Through this, I was able to achieve a final result which I aggregated and obtain the count of individual word 
items.

![substring](https://github.com/equanimittyy/mobydick/assets/104692345/07f800fd-9e10-434c-a2bf-ea44f418d8e6)


### Visualisation in PBI -
With clean data imported into PowerBI, creating the visualisations and slicers required for my work was quite easy. No difficulties
were encountered when importing the data and creating my visualisation.

![PBIVIZ](https://github.com/equanimittyy/mobydick/assets/104692345/2db2ced6-3915-46fc-a876-ce67c8517e05)


## Limitations:
There were a few limitations to this project. Assessing the accuracy of my data extraction and cleaning processes, it seems that
the data drawn through my Python is not comprehensive and complete as the final word count is quite a significant number less than
the actual word count found in the book.

Further, limitations such as the words in the headers themselves not appearing in the 'content' word count contribute to further
inaccuracy and incompleteness. Perhaps a more comprehensive analysis as to why data was missing for a significant portion of the
book is in order to identify the source of incompleteness, however, I gather that this was a result of a flawed extraction process
in Python and incorrect handling of the 'h2' HTML element and it's complexities.

![PyHTMLh2](https://github.com/equanimittyy/mobydick/assets/104692345/3021cd2c-c421-47be-84c7-9e837ba07a27)

![HTML](https://github.com/equanimittyy/mobydick/assets/104692345/ddea86ce-8d19-42af-9c2e-20d8f6fd3ea7)

> [!Note] 
> _See the incorrect handling of the "h2" element in the above. The 'ETYMOLOGY' section of the book is captured as if it was a Chapter of the book._

### Closing Remarks:
Overall, the project itself was quite enjoyable as I had succeeded in completing my objective of extracting, transforming and loading
data from a real, live website with only what I would consider foundational skills. The experience has been quite insightful as it has 
helped me identify where I may need to devote further time towards, and reinvigorated my confidence in my ability to learn.

I find that my time spent towards improving my SQL skills through third-party resources were well spent, and look forward to improving my
skills in both and outside SQL in order to widen my breath of technical/practical experience and allow myself to tackle more challenging
work.
